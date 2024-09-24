---
source: "blog"
title: "anitagraser.com: Building spatial analysis assistants using OpenAI’s Assistant API"
image: "building-spatial-analysis-assistants-using-openais-assistant-api."
date: "2024-08-29"
link: "https://anitagraser.com/2024/08/29/building-spatial-analysis-assistants-using-openais-assistant-api/"
draft: "true"
showcase: "planet"
---

<p>Earlier this year, I shared my experience using ChatGPT’s Data Analyst web interface for analyzing spatiotemporal data in the post <a href="https://anitagraser.com/2024/05/30/chatgpt-data-analyst-vs-movement-data/">&#8220;ChatGPT Data Analyst vs. Movement Data&#8221;</a>. The Data Analyst web interface, while user-friendly, is not equipped to handle all types of spatial data tasks, particularly those involving more complex or large-scale datasets. Additionally, because the code is executed on a remote server, we&#8217;re limited to the libraries and tools available in that environment. I&#8217;ve often encountered situations where the Data Analyst simply doesn’t have access to the necessary libraries in its Python environment, which can be frustrating if you need specific GIS functionality.</p>



<p>Today, we&#8217;ll therefore start to explore alternatives to ChatGPT’s Data Analyst Web Interface, specifically, the <strong>OpenAI Assistant API</strong>. Later, I plan to dive deeper into even more flexible approaches, like <strong>Langchain&#8217;s Pandas DataFrame Agents</strong>. We’ll explore these options using spatial analysis workflow, such as: </p>



<ol class="wp-block-list">
<li>Loading a zipped shapefile and investigate its content</li>



<li>Finding the three largest cities in the dataset</li>



<li>Selecting all cities in a region, e.g. in Scandinavia from the dataset</li>



<li>Creating static and interactive maps</li>
</ol>



<p>To try the code below, you&#8217;ll need an OpenAI account with a few dollars on it. While gpt-3.5-turbo is quite cheap, using gpt-4o with the Assistant API can get costly fast. </p>



<h3 class="wp-block-heading"><strong>OpenAI Assistant API</strong></h3>



<p>The OpenAI Assistant API allows us to create a custom data analysis environment where we can interact with our spatial datasets programmatically. To write the following code, I used the assistant <a href="https://platform.openai.com/docs/assistants/quickstart">quickstart</a> and related docs (yes, shockingly, ChatGPT wasn&#8217;t very helpful for writing this code).</p>



<p>Like with Data Analyst, we need to upload the zipped shapefile to the server to make it available to the assistant. Then we can proceed to ask it questions and task it to perform analytics and create maps.</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from openai import OpenAI

client = OpenAI()

file = client.files.create(
  file=open("H:/ne_110m_populated_places_simple.zip", "rb"),
  purpose='assistants'
)
</pre></div>


<p>Then we can hand the file over to the assistant:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
assistant = client.beta.assistants.create(
  name="GIS Analyst",
  instructions="You are a personal GIS data analyst. Write and rund code to answer geospatial analysis questions",
  tools=&#91;{"type": "code_interpreter"}],
  model="gpt-3.5-turbo",  # or "gpt-4o"
  tool_resources={
    "code_interpreter": {
      "file_ids": &#91;file.id]
    }
  }  
)
</pre></div>


<p>Then we can start asking questions and giving our assistant tasks:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="Please load the zipped shapefile and describe the content"
)
</pre></div>


<pre class="wp-block-code"><code>assistant &gt; The shapefile has been successfully loaded as a GeoDataFrame with the following details:

- The GeoDataFrame has 243 entries.
- It contains a total of 38 columns with various data types including integer, float, and object types.
- One of the columns is a geometry column representing the spatial information.

If you have any specific analysis or visualizations you would like to perform on this data, feel free to let me know!</code></pre>



<p>The docs have a nice example for how to stream the answers back, e.g. into a Jupyter notebook. I&#8217;ve used it to create a small convenience function: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
def ask_another_question(question):
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=question
    )
    with client.beta.threads.runs.stream(
        thread_id=thread.id,
        assistant_id=assistant.id,
        event_handler=EventHandler(),
    ) as stream:
        stream.until_done()

ask_another_question("Please list the three largest cities")
</pre></div>


<pre class="wp-block-code"><code>assistant &gt; code_interpreter

# Sort the GeoDataFrame by the population in descending order
largest_cities = gdf.sort_values(by='pop_max', ascending=False).head(3)&#091;&#091;'name', 'pop_max']]
largest_cities
assistant &gt; The three largest cities in the dataset, along with their maximum population numbers, are as follows:

1. Tokyo: 35,676,000
2. New York: 19,040,000
3. Mexico City: 19,028,000

These cities have the highest recorded maximum population numbers in the dataset. Let me know if you need any further information or analysis!</code></pre>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
ask_another_question("extract all scandinavian cities ")
</pre></div>


<pre class="wp-block-code"><code>assistant &gt; To extract all the Scandinavian cities from the dataset, we can filter the GeoDataFrame based on the countries typically considered part of Scandinavia. These countries include Norway, Sweden, Denmark, Finland, and sometimes Iceland. Let's filter the GeoDataFrame to extract the Scandinavian cities.
assistant &gt; code_interpreter

# List of countries typically considered part of Scandinavia
scandinavian_countries = &#091;'Norway', 'Sweden', 'Denmark', 'Finland', 'Iceland']

# Filter the GeoDataFrame for Scandinavian cities
scandinavian_cities = gdf&#091;gdf&#091;'adm0name'].isin(scandinavian_countries)]&#091;&#091;'name', 'adm0name']]

scandinavian_cities.head()  # Displaying the first few Scandinavian cities
assistant &gt; Here are some of the Scandinavian cities extracted from the dataset:

1. Reykjavík, Iceland
2. Oslo, Norway
3. Helsinki, Finland
4. København (Copenhagen), Denmark
5. Stockholm, Sweden

These are just a few examples of Scandinavian cities present in the dataset. If you would like the complete list or perform any specific analysis on these cities, feel free to let me know!</code></pre>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
ask_another_question(
    "please create a world map with all cities (use gray circles) "
    "with scandinavian cities highlighted as red circles. "
)
</pre></div>


<pre class="wp-block-code"><code>assistant &gt; To create a world map with all cities represented as gray circles and Scandinavian cities highlighted as red circles, we will use the GeoPandas library for mapping. Let's go ahead and create the map.
assistant &gt; code_interpreter

import matplotlib.pyplot as plt

# Plot all cities with gray circles and Scandinavian cities with red circles
fig, ax = plt.subplots(figsize=(12, 8))

# Plot all cities in gray circles
gdf.plot(ax=ax, color='lightgrey', markersize=5)

# Plot Scandinavian cities in red circles
scandinavian_cities.plot(ax=ax, color='red', markersize=50, edgecolor='black', label='Scandinavian Cities')

# Set the title
ax.set_title('World Map with Scandinavian Cities Highlighted', fontsize=16)

# Add legend
ax.legend()

# Display the map
plt.show()
assistant &gt; It seems that there was an error while plotting the map because the GeoDataFrame `scandinavian_cities` does not have the necessary numeric data to plot the map directly.
...
plt.show()

output &gt;

assistant &gt; Here is the world map with all cities represented as gray circles and Scandinavian cities highlighted as red circles. The map provides a visual representation of the locations of the Scandinavian cities in relation to the rest of the cities around the world. If you need any further assistance or modifications, feel free to let me know!</code></pre>



<p>To load and show the image, we can use: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image():
    messages = client.beta.threads.messages.list(thread_id=thread.id)

    for m in messages.data:
        if m.role == "user":
            continue
        if m.content&#91;0].type == 'image_file':
            m.content&#91;0].image_file.file_id
            image_data = client.files.content(messages.data&#91;0].content&#91;0].image_file.file_id)
            image_data_bytes = image_data.read()
            with open("./out/my-image.png", "wb") as file:
                file.write(image_data_bytes)
            image = mpimg.imread("./out/my-image.png")
            plt.imshow(image)
            plt.box(False)
            plt.xticks(&#91;])
            plt.yticks(&#91;])
            plt.show() 
            break
</pre></div>


<figure class="wp-block-image size-large"><img alt="" class="wp-image-9172" height="408" src="https://anitagraser.com/wp-content/uploads/2024/08/image-6.png?w=544" tabindex="0" width="544" /></figure>



<p>Asking for an interactive map in an html file works in a similar fashion. </p>



<p>You can see the whole analysis workflow it in action here:</p>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<div class="embed-youtube"></div>
</div></figure>



<p>This way, we can use ChatGPT to perform data analysis from the comfort of our Jupyter notebooks. However, it&#8217;s important to note that, like the Data Analyst, the code we execute with the Assistant API runs on a remote server. So, again, we are restricted to the libraries available in that server environment. This is an issue we will address next time, when we look into Langchain. </p>



<h3 class="wp-block-heading"><strong>Conclusion</strong></h3>



<p>ChatGPT’s Data Analyst Web Interface and  the OpenAI Assistant API both come with their own advantages and disadvantages.</p>



<p>The results can be quite random. In the  Scandinavia example, every run can produce slightly different results. Sometimes the results just use different assumptions such as, e.g. Finland and Iceland being part of Scandinavia or not, other times, they can be outright wrong.</p>



<p>As always, I’m interested to hear your experiences and thoughts. Have you been testing the LLM plugins for QGIS when they originally came out? </p>
