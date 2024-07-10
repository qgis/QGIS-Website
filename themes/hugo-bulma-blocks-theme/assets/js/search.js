{{/* Note: This file needs to be rendered as a template in HUGO
     in order to ensure urls referenced are correct. See header.html in layouts
     for template rendering implementation. TS */}}

var summaryInclude = 180;
var fuseOptions = {
    shouldSort: true,
    includeMatches: true,
    includeScore: true,
    tokenize: true,
    matchAllTokens: true,
    location: 0,
    distance: 5000, // Increase this for deeper search based on content character length
    threshold: 0.55,
    minMatchCharLength: 2,
    keys: [
        {name: "title", weight: 0.45},
        {name: "contents", weight: 0.4},
        {name: "tags", weight: 0.1},
        {name: "categories", weight: 0.05}
    ]
};

// =============================
// Search
// =============================

var inputBox = document.getElementById('search-query');
if (inputBox !== null) {
    var searchQuery = param("q");
    if (searchQuery) {
        inputBox.value = searchQuery || "";
        executeSearch(searchQuery, false);
    } else {
        var results = document.getElementById('search-results')
        if (results != null) {
            results.innerHTML = 
            '<p class="search-results-empty">Please enter a word or phrase above, or see <a href="{{ "tags/" | absURL }}">all tags</a>.</p>';
        }
    }
}

function executeSearch(searchQuery) {

    show(document.querySelector('.search-loading'));

    fetch('{{ "index.json" | absURL }}').then(function (response) {
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' + response.status);
            return;
        }
        // Examine the text in the response
        response.json().then(function (pages) {
            var fuse = new Fuse(pages, fuseOptions);
            var result = fuse.search(searchQuery);
            if (result.length > 0) {
                populateResults(result);
            } else {
                document.getElementById('search-results').innerHTML = 
                '<p class=\"search-results-empty\">No matches found</p>';
            }

            // result var may contain invalid items, and inner html remains empty. show "Not found" then
            if (document.getElementById('search-results').innerHTML == '')
                document.getElementById('search-results').innerHTML = 
                    '<p class=\"search-results-empty\">No matches found</p>';

            hide(document.querySelector('.search-loading'));
        })
        .catch(function (err) {
            console.log('Fetch Error :-S', err);
        });
    });
}

function populateResults(results) {
    var searchQuery = document.getElementById("search-query").value;
    var searchResults = document.getElementById("search-results");
    
    // Clear previous results
    searchResults.innerHTML = "";

    // Tokenize the search query to handle multiple words
    var searchTokens = searchQuery.split(/\s+/).filter(token => token.length > 0);
    
    // Pull template from Hugo template definition
    var templateDefinition = document.getElementById("search-result-template").innerHTML;

    results.forEach(function (value, key) {
        var contents = value.item.contents;
        var snippet = "";
        var snippetHighlights = [];

        // Build the snippet and highlight tokens
        snippetHighlights.push(...searchTokens);
        snippet = createSnippet(contents, searchTokens);

        // Replace values for tags
        var tags = "";
        if (value.item.tags) {
            value.item.tags.forEach(function (element) {
                tags += "<span class='tag is-warning'><a href='/tags/" + element + "'>" + element + "</a></span> ";
            });
        }
        
        // Replace values for categories
        var categories = "";
        if (value.item.categories) {
            value.item.categories.forEach(function (element) {
                categories += "<span class='tag is-danger'><a href='/categories/" + element + "'>" + element + "</a></span> ";
            });
        }

        // Render the output using the template
        var output = render(templateDefinition, {
            key: key,
            title: value.item.title,
            link: value.item.permalink,
            tags: tags,
            categories: categories,
            snippet: snippet
        });

        // Check if output matches any of the search tokens
        var matchFound = searchTokens.some(token => output.toLowerCase().includes(token.toLowerCase()));

        // Append the output to the search results if there is a match
        if (matchFound) {
            searchResults.innerHTML += output;

            // Highlight each token in the snippet
            snippetHighlights.forEach(function (snipvalue) {
                var instance = new Mark(document.getElementById('summary-' + key));
                instance.mark(snipvalue);
            });
        }
    });
}

function createSnippet(contents, tokens) {
    const snippetLength = 200;
    let start = 0;
    let end = snippetLength;
    tokens.forEach(token => {
        let tokenPosition = contents.toLowerCase().indexOf(token.toLowerCase());
        if (tokenPosition > -1) {
            start = Math.max(0, tokenPosition - 50);
            end = Math.min(contents.length, tokenPosition + snippetLength - 50);
        }
    });
    let snippet = contents.substring(start, end);
    if (start > 0) {
        snippet = '&hellip;' + snippet;
    }
    if (end < contents.length) {
        snippet += '&hellip;';
    }
    return snippet;
}

function render(templateString, data) {
    var conditionalMatches, conditionalPattern, copy;
    conditionalPattern = /\$\{\s*isset ([a-zA-Z]*) \s*\}(.*)\$\{\s*end\s*}/g;
    //since loop below depends on re.lastInxdex, we use a copy to capture any manipulations whilst inside the loop
    copy = templateString;
    while ((conditionalMatches = conditionalPattern.exec(templateString)) !== null) {
        if (data[conditionalMatches[1]]) {
            //valid key, remove conditionals, leave contents.
            copy = copy.replace(conditionalMatches[0], conditionalMatches[2]);
        } else {
            //not valid, remove entire section
            copy = copy.replace(conditionalMatches[0], '');
        }
    }
    templateString = copy;
    //now any conditionals removed we can do simple substitution
    var key, find, re;
    for (key in data) {
        find = '\\$\\{\\s*' + key + '\\s*\\}';
        re = new RegExp(find, 'g');
        templateString = templateString.replace(re, data[key]);
    }
    return templateString;
}

// Helper Functions
function show(elem) {
    elem.style.display = 'block';
}
function hide(elem) {
    elem.style.display = 'none';
}
function param(name) {
    return decodeURIComponent((location.search.split(name + '=')[1] || '').split('&')[0]).replace(/\+/g, ' ');
}
