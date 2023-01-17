{{/* Note: This file needs to be rendered as a template in HUGO
     in order to ensure urls referenced are correct. See header.html in layouts
     for template rendering implementation. TS */}}

var summaryInclude = 180;
var fuseOptions = {
    shouldSort: true,
    includeMatches: true,
    includeScore: true,
    tokenize: true,
    location: 0,
    distance: 100,
    minMatchCharLength: 1,
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

    // pull template from hugo template definition
    var templateDefinition = document.getElementById("search-result-template").innerHTML;

    results.forEach(function (value, key) {

        var contents = value.item.contents;
        var snippet = "";
        var snippetHighlights = [];

        snippetHighlights.push(searchQuery);
        snippet = contents.substring(0, summaryInclude * 2) + '&hellip;';

        //replace values
        var tags = ""
        if (value.item.tags) {
            value.item.tags.forEach(function (element) {
                tags = tags + "<span class='tag is-warning'><a href='{{ "tags/" | absURL }}" + element + "'>" + element + "</a></span>"
            });
        }
        var categories = ""
        if (value.item.categories) {
            value.item.categories.forEach(function (element) {
                categories = categories + "<span class='tag is-danger'><a href='{{ "categories/" | absURL }}" + element + "'>" + element + "</a></span>"
            });
        }        

        var output = render(templateDefinition, {
            key: key,
            title: value.item.title,
            link: value.item.permalink,
            tags: tags,
            categories: categories,
            snippet: snippet
        });
        if (output.includes(searchQuery))
        {
            searchResults.innerHTML += output;
        }
        snippetHighlights.forEach(function (snipvalue, snipkey) {
            var instance = new Mark(document.getElementById('summary-' + key));
            instance.mark(snipvalue);
        });

    });
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
