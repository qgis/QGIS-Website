---
date: '2023-05-21'
draft: 'true'
image: analyzing-video-based-bicycle-trajectories.
link: https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/
showcase: planet
source: blog
title: 'anitagraser.com: Analyseren van op video gebaseerde fietstrajecten'

---
<p>Wist u dat <a href="https://movingpandas.org">MovingPandas</a> ook coördinaten voor lokale afbeeldingen ondersteunt? Inderdaad, dat doet het.</p>

<p>In de post van vandaag zullen we verkennen hoe we deze mogelijkheid kunnen gebruiken om fietstochten te analyseren die zijn uitgenomen uit videomateriaal, gepubliceerd door <a href="https://fosstodon.org/@mszll@datasci.social">Michael Szell @mszll</a>: </p>

<ul>
<li>Gegevensset: <a href="https://zenodo.org/record/7288616" rel="nofollow">https://zenodo.org/record/7288616</a>  </li>

<li>Beschrijving gegevens: <a href="https://arxiv.org/abs/2211.01301" rel="nofollow">https://arxiv.org/abs/2211.01301</a></li>
</ul>

<p>De coördinaten voor het fietstraject zijn opgeslagen in twee afzonderlijke lijsten: xs_640x360 en ys640x360:</p>

<figure class="wp-block-image size-large"><img data-attachment-id="8453" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-4-7/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-4.png" data-orig-size="1043,463" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-4" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-4.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-4.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-4.png?w=1024" alt="" class="wp-image-8453" srcset="https://underdark.files.wordpress.com/2023/05/image-4.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/05/image-4.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-4.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-4.png?w=768 768w, https://underdark.files.wordpress.com/2023/05/image-4.png 1043w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>

<p>Deze indeling lijkt enigszins op die van de Kaggle Taxi gegevensset waarmee we werkten in <a href="https://anitagraser.com/2023/05/12/how-to-use-kaggles-taxi-trajectory-data-in-movingpandas/">de vorige post</a>. Echter, om de oplossing te kunnen gebruiken die we hier hebben geïmplementeerd, moeten we de X- en Y-coördinaten combineren in nette tuples (x,y):</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
df&#91;'coordinates'] = df.apply(
    lambda row: list(zip(row&#91;'xs_640x360'], row&#91;'ys_640x360'])), axis=1)
df.drop(columns=&#91;'xs_640x360', 'ys_640x360'], inplace=True)
</pre></div>

<p>Hierna kunnen we de punten maken en de juiste tijdstempels berekenen uit de framenummers:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
def compute_datetime(row):
    # hier gebeurt enig beredeneerd gokwerk: de paper vermeld dat de video gaat over 2021-06-09 07:00-08:00
    d = datetime(2021,6,9,7,0,0) + (row&#91;'frame_in'] + row&#91;'running_number']) * timedelta(seconds=2)
    return d
def create_point(xy):
    try: 
        return Point(xy)
    except TypeError:  # als er waarden nan in de invoergegevens staan
        return None
new_df = df.head().explode('coordinates')
new_df&#91;'geometry'] = new_df&#91;'coordinates'].apply(create_point)
new_df&#91;'running_number'] = new_df.groupby('id').cumcount()
new_df&#91;'datetime'] = new_df.apply(compute_datetime, axis=1)
new_df.drop(columns=&#91;'coordinates', 'frame_in', 'running_number'], inplace=True)
new_df
</pre></div>

<p>Als d epunten en tijdstempels eenmaal gereed zijn, kunnen we de MovingPandas TrajectoryCollection maken. Merk op dat we expliciet vermelden dat er geen CRS voor deze gegevensset is (crs=None):</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
trajs = mpd.TrajectoryCollection(
    gpd.GeoDataFrame(new_df), 
    traj_id_col='id',  t='datetime', crs=None)
</pre></div>

<h2 class="wp-block-heading">Plotten van trajecten met coördinaten van afbeeldingen</h2>

<p>Soortgelijk, om deze trajecten te plotten, zouden we hvplot moeten vertellen dat het geen tegels voor de achtergrondkaart moet ophalen (&#8217;tiles&#8217;:None) en dat de coördinaten niet geografisch zijn (&#8216;geo&#8217;:False):</p>

<figure class="wp-block-image size-large"><img data-attachment-id="8467" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-11-4/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-11.png" data-orig-size="746,550" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-11" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-11.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-11.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-11.png?w=746" alt="" class="wp-image-8467" srcset="https://underdark.files.wordpress.com/2023/05/image-11.png 746w, https://underdark.files.wordpress.com/2023/05/image-11.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-11.png?w=300 300w" sizes="(max-width: 746px) 100vw, 746px" /></figure>

<p>Als u de volledige broncode wilt verkennen is mijn fork van Github, met het Jupyter notebook, te vinden op: <a href="https://github.com/anitagraser/desirelines/blob/main/mpd.ipynb" rel="nofollow">https://github.com/anitagraser/desirelines/blob/main/mpd.ipynb</a></p>

<p>De opslagplaats bevat ook een camera-afbeelding van de kruising, die kan dienen als achtergrond voor onze plots van het traject:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
bg_img = hv.RGB.load_image('img/intersection2.png', bounds=(0,0,640,360)) 
</pre></div>

<figure class="wp-block-image size-large"><img data-attachment-id="8466" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-10-4/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-10.png" data-orig-size="751,492" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-10" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-10.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-10.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-10.png?w=751" alt="" class="wp-image-8466" srcset="https://underdark.files.wordpress.com/2023/05/image-10.png 751w, https://underdark.files.wordpress.com/2023/05/image-10.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-10.png?w=300 300w" sizes="(max-width: 751px) 100vw, 751px" /></figure>

<p>Een belangrijke valkuil is dat snelheid zal worden berekend in pixels per seconde. Dus als we de snelheid voor de fiets plotten, zullen de segmenten, die dichter bij de camera liggen, sneller verschijnen dan de segmenten op de achtergrond:</p>

<figure class="wp-block-image size-large"><img data-attachment-id="8450" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-3-7/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-3.png" data-orig-size="812,492" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-3" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-3.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-3.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-3.png?w=812" alt="" class="wp-image-8450" srcset="https://underdark.files.wordpress.com/2023/05/image-3.png 812w, https://underdark.files.wordpress.com/2023/05/image-3.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-3.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-3.png?w=768 768w" sizes="(max-width: 812px) 100vw, 812px" /></figure>

<p>Om dat op te lossen zouden we de vervormingen van de cameralens en het perspectief moeten corrigeren. Ik ben er zeker van dat er gespecialiseerde software voor die taak is, maar voor het doel van deze post grijp ik de kans aan om eindelijk de plug-in <a href="https://plugins.qgis.org/plugins/VectorBender/">VectorBender</a> eens te testen.</p>

<h2 class="wp-block-heading">Geoverwijzingen maken voor de trajecten met QGIS plug-in VectorBender</h2>

<p>Laten we de vijf testtrajecten en de camera-afbeelding laden in QGIS. Om er zeker van te zijn dat ze goed uitlijnen, zijn beide ingesteld op hetzelfde CRS en heb ik het volgende basis wereldbestand voor de camera-afbeelding gemaakt:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: plain; title: ; notranslate">
1
0
0
-1
0
360
</pre></div>

<p>Dan kunnen we de gereedschappen van VectorBender gebruiken om de trajecten te voorzien van geoverwijzingen door locaties van de camera-afbeelding te koppelen aan locaties op luchtfoto's. U kunt het hele proces hier in actie zien: </p>

<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe class="youtube-player" width="545" height="307" src="https://www.youtube.com/embed/LP6oKEUgX30?version=3&#038;rel=1&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;fs=1&#038;hl=en&#038;autohide=2&#038;wmode=transparent" allowfullscreen="true" style="border:0;" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation"></iframe>
</div></figure>

<p>Na ongeveer 15 minuten van koppelen van controlepunten, komt VectorBender met het volgende resultaat voor het traject met geoverwijzingen: </p>

<figure class="wp-block-image size-large"><img data-attachment-id="8463" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-9-4/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-9.png" data-orig-size="1532,1087" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-9" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-9.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-9.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-9.png?w=1024" alt="" class="wp-image-8463" srcset="https://underdark.files.wordpress.com/2023/05/image-9.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/05/image-9.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-9.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-9.png?w=768 768w, https://underdark.files.wordpress.com/2023/05/image-9.png 1532w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>

<p>Niet slecht voor een snelle-en-vuile hack. Sommige punten aan de randen van de afbeelding zouden niet kunnen zijn voorzien van geoverwijzingen, omdat ik niet altijd in staat was om geschikte controlepunten te identificeren op de randen van de camera-afbeelding. Het is dus niet perfect, maar zou de schattingen voor de snelheid moeten verbeteren.</p>

<hr class="wp-block-separator has-alpha-channel-opacity" />

<p>Deze post is een deel van een serie. Lees meer over&nbsp;<a href="https://anitagraser.com/movement-data-in-gis/">gegevens over verplaatsingen in GIS.</a></p>

<p></p>

