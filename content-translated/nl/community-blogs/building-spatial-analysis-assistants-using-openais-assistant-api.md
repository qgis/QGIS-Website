---
date: '2024-08-29'
draft: 'true'
image: building-spatial-analysis-assistants-using-openais-assistant-api.
link: https://anitagraser.com/2024/08/29/building-spatial-analysis-assistants-using-openais-assistant-api/
showcase: planet
source: blog
title: 'anitagraser.com: Assistenten voor ruimtelijke analyses bouwen met OpenAI’s
  Assistant API'

---
<p>Eerder dit jaar deelde ik mijn ervaring met het gebruiken van ChatGPT’s Data Analyst webinterface voor het analyseren van tijd-ruimtelijke gegevens in de post <a href="https://anitagraser.com/2024/05/30/chatgpt-data-analyst-vs-movement-data/">&#8220;ChatGPT Data Analyst vs. Movement Data&#8221;</a>. De Data Analyst webinterface, hoewel gebruikersvriendelijk, is niet uitgerust om alle taken voor ruimtelijke gegevens af te handelen, in het bijzonder die welke meer complexe of grootschalige gegevenssets betreffen. Aanvullend, omdat de code wordt uitgevoerd op een server op afstand, zijn we beperkt tot de bibliotheken en programma's die in die omgeving beschikbaar zijn. Ik ben vaak situaties tegengekomen waar de Data Analyst eenvoudigweg geen toegang heeft tot de noodzakelijke bibliotheken van zijn omgeving van Python, wat frustrerend kan zijn als je specifieke functionaliteit voor GIS nodig hebt.</p>

<p>vandaag zullen we daarom beginnen met het verkennen van alternatieven voor ChatGPT’s Data Analyst Web Interface, specifiek de <strong>OpenAI Assistant API</strong>. Later plan ik om dieper in te gaan op zelfs meer flexibelere benaderingen, zoals <strong>Langchain&#8217;s Pandas DataFrame Agents</strong>. We zullen deze opties verkennen met een werkstroom voor ruimtelijke analyse, zoals: </p>

<ol class="wp-block-list">
<li>Laden van een gezipt Shapefile en de inhoud ervan onderzoeken</li>

<li>Zoeken naar de drie grootste steden in de gegevensset</li>

<li>Selecteren van alle steden in een regio, bijv. in Scandinavië, uit de gegevensset</li>

<li>Statische en interactieve kaarten maken</li>
</ol>

<p>U heeft, om de onderstaande code te kunnen uitvoeren, een account van OpenAI met een tegoed van enkele dollars nodig. Hoewel gpt-3.5-turbo vrij goedkoop is, kunnen de kosten voor het gebruiken van gpt-4o met de Assistant API snel oplopen. </p>

<h3 class="wp-block-heading"><strong>OpenAI Assistant API</strong></h3>

<p>De OpenAI Assistant API stelt ons in staat om een aangepaste omgeving voor gegevensanalyse te maken, waar we programmatisch met onze ruimtelijke gegevenssets kunnen interacteren. Ik gebruikte, om de volgende code te schrijven, de assistent <a href="https://platform.openai.com/docs/assistants/quickstart">quickstart</a> en gerelateerde documenten (ja, schokkend genoeg was ChatGPT niet echt hulpvaardig bij het schrijven van deze code).</p>

<p>Net als met Data Analyst, moeten we het gezipte Shapefile uploaden naar de server om het beschikbaar te maken voor de assistent. Daarna kunnen we doorgaan om het vragen te stellen en het taken voor analyses en het maken van kaarten te laten uitvoeren.</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from openai import OpenAI

client = OpenAI()

file = client.files.create( file=open("H:/ne_110m_populated_places_simple.zip", "rb"), purpose='assistants' ) </pre></div>

<p>Daarna kunnen we het bestand overhandigen aan de assistent:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
assistant = client.beta.assistants.create(
  name="GIS Analyst",
  instructions="U bent een persoonlijke gegevensanalist voor GIS. Schrijf en voer code uit om vragen over georuimtelijke analyses te beantwoorden",
  tools=&#91;{"type": "code_interpreter"}],
  model="gpt-3.5-turbo",  # of "gpt-4o"
  tool_resources={
    "code_interpreter": {
      "file_ids": &#91;file.id]
    }
  }  
)
</pre></div>

<p>Dan kunnen we beginnen met het stellen van vragen en onze assistent taken opgeven:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
thread = client.beta.threads.create()

message = client.beta.threads.messages.create( thread_id=thread.id, role="user", content="Laad het gezipte Shapefile en beschrijf de inhoud" ) </pre></div>

<pre class="wp-block-code"><code>assistant &gt; De Shapefile is met succes geladen als een GeoDataFrame met de volgende details:

- De GeoDataFrame heeft 243 items.
- Het bevat in totaal 38 kolommen met verschillende typen gegevens, inclusief integer, float en typen objecten.
- Een van de kolommen is een kolom geometrie die de ruimtelijke informatie weergeeft.

Als u specifieke analyses of visualisaties heeft die u op deze gegevens uit zou willen laten voeren, laat het mij dan maar weten!</code></pre>

<p>De documenten hebben een leuk voorbeeld voor hoe de antwoorden terug te laten stromen, bijv. in een Jupyter notebook. Ik gebruikte het om een kleine handige functie te maken: </p>

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

ask_another_question("Vermeld de drie grootste steden") </pre></div>

<pre class="wp-block-code"><code>assistant &gt; code_interpreter

# Sorteert het GeoDataFrame op de bevolking in aflopende volgorde
largest_cities = gdf.sort_values(by='pop_max', ascending=False).head(3)&#091;&#091;'name', 'pop_max']]
largest_cities
assistant &gt; De drie grootste steden in de gegevensset, met daarnaast hun cijfers voor de maximale bevolking, zijn als volgt:

1. Tokio: 35,676,000
2. New York: 19,040,000
3. Mexico City: 19,028,000

Deze steden hebben de hoogste vermelde maximale cijfers voor bevolking in de gegevensset. Laat het me weten als u meer informatie of analyse wilt!</code></pre>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
ask_another_question("neem alle Scandinavische steden uit ")
</pre></div>

<pre class="wp-block-code"><code>assistant &gt; Voor het uitnemen van alle Scandinavische steden uit de gegevensset, kunen we de GeoDataFrame filteren, gebaseerd op de landen die geoonwlijk worden gerekend als een deel van Scandinavië. Deze landne omvatten Noorwegen, Zweden, Denemarken, Finland en soms IJsland. Laten we de GeoDataFrame filteren om de Scandinavische steden uit te nemen.
assistant &gt; code_interpreter

# Lijst met landen die gewoonlijk worden beschouwd als een deel van Scandinavië
scandinavian_countries = &#091;'Norway', 'Sweden', 'Denmark', 'Finland', 'Iceland']

# Filter de GeoDataFrame op Scandinavische steden
scandinavian_cities = gdf&#091;gdf&#091;'adm0name'].isin(scandinavian_countries)]&#091;&#091;'name', 'adm0name']]

scandinavian_cities.head()  # Weergeven van de eerste paar Scandinavische steden
assistant &gt; Hier zijn enkele van de Scandinavische steden die uit de gegevensset zijn uitgenomen:

1. Reykjavík, Iceland
2. Oslo, Norway
3. Helsinki, Finland
4. København (Copenhagen), Denmark
5. Stockholm, Sweden

Dit zijn slechts enkele voorbeelden van Scandinavische steden die in de gegevensset aanwezig zijn. Als u de volledige lijst wilt of een specifieke analyse op deze steden wilt uitvoeren, laat het me dan maar weten!</code></pre>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
ask_another_question(
    "maak ene wereldkaart met alle steden (gebruik grijze cirkels) "
    "waarin Scandinavische steden zijn geaccentueerd als rode cirkels. "
)
</pre></div>

<pre class="wp-block-code"><code>assistant &gt; Voor het maken van een wereldkaart, waarop alle steden worden weergegeven als grijze cirkels en Scandinavische steden worden geaccentueerd als rode cirkels, zullen we de bibliotheek GeoPandas gebruiken voor het in kaart brengen. Laten we doorgaan en de kaart maken.
assistant &gt; code_interpreter

import matplotlib.pyplot as plt

# Plot alle steden met grijze cirkels en Scandinavische steden met rode cirkels
fig, ax = plt.subplots(figsize=(12, 8))

# Plot alle steden in grijze cirkels
gdf.plot(ax=ax, color='lightgrey', markersize=5)

# Plot Scandinavische steden in rode cirkels
scandinavian_cities.plot(ax=ax, color='red', markersize=50, edgecolor='black', label='Scandinavische steden')

# Set the title
ax.set_title('Wereldkaart met Scandinavische steden geaccentueerd', fontsize=16)

# Toevoegen legenda
ax.legend()

# De kaart weergeven
plt.show()
assistant &gt; Het lijkt erop dat er ene fout optrad bij het plotten van de kaart, omdat de GeoDataFrame `scandinavian_cities` niet de noodzakelijke numerieke gegevens heeft om de kaart direct te plotten.
...
plt.show()

output &gt;

assistant &gt; Hier is de wereldkaart met alle steden weergegeven als grijze cirkels en de Scandinavische steden als rode cirkels. De kaart verschaft een visuele weergave van de locaties van de Scandinavische steden in relatie tot de rest van de steden in de wereld. Als u verder nog assistentie of aanpassingen wilt, laat het me dan maar weten!</code></pre>

<p>We kunnen, om de afbeelding te laden en weer te geven, gebruiken: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image(): messages = client.beta.threads.messages.list(thread_id=thread.id)

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

<p>Vragen om een interactieve kaart in een HTML-bestand werkt op een soortgelijke manier. </p>

<p>U kunt de gehele werkstroom voor de analyse hier in actie zien:</p>

<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<div class="embed-youtube"></div>
</div></figure>

<p>Op deze manier kunnen we ChatGPT gebruiken om gegevensanalyse uit te voeren met het comfort van onze Jupyter notebooks. Het is echter belangrijk om op te merken dat, net als met de Data Analyst, de code die we uitvoeren met de Assistant API wordt uitgevoerd op ene server op afstand. Dus, opnieuw, zijn we beperkt tot de beschikbare bibliotheken in de omgeving van die server. Dat is een probleem dat we de volgende keer zullen behandelen, als we kijken naar Langchain. </p>

<h3 class="wp-block-heading"><strong>Conclusie</strong></h3>

<p>ChatGPT’s Data Analyst Web Interface en de OpenAI Assistant API hebben beide hun eigen voor- en nadelen.</p>

<p>De resultaten kunnen vrij willekeurig zijn. In het voorbeeld van  Scandinavië, kan elke uitvoering enigszins verschillende resultaten produceren. Soms gebruiken de resultaten gewoon andere aannames, zoals bijv. dat Finland en IJsland deel van Scandinavië zijn of niet, andere keren, kunnen ze gewoon fout zijn.</p>

<p>Zoals altijd ben ik zeer geïnteresseerd om uw ervaringen en gedachten te horen. Heeft u de plug-ins voor LLM voor QGIS getest toen ze origineel beschikbaar werden? </p>

