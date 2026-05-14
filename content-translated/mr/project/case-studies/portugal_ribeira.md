---
HasBanner: false
archived: true
date: 2012-07-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_ribeira1.png
title: उत्तर पोर्तुगाल मधील लांडग्यांसाठी इकोलॉजिकल कॉरिडोरचे मॉडेलिंग करण्यासाठी
  क्यूजीआयएस आणि ग्रास
type: case-study

---
{{<content-start >}}
# उत्तर पोर्तुगाल मधील लांडग्यांसाठी इकोलॉजिकल कॉरिडोरचे मॉडेलिंग करण्यासाठी क्यूजीआयएस आणि ग्रास
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2012</span>
</p>

The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

<figure>
<img src="../images/portugal_ribeira1.png" class="align-right" alt="portugal_ribeira1.png" />
<figcaption>Study area in Portugal</figcaption>
</figure>

रिबिरा दे पेना ही पोर्तुगालच्या उत्तरेस असलेल्या विला रियल जिल्ह्यातील एक नगरपालिका आहे. ही एक ग्रामीण नगरपालिका आहे, शेती, चरणे पशुधन, वन, पर्वत, दle्या आणि विविध जीवजंतू आणि कमी मानवी घनतेसह, निवारा आणि अन्न पुरवते. कठोर आणि डोंगराळ ट्रायस-ओस-मॉन्टेस आणि हिरवळ मिन्हो यांच्यातील संक्रमण क्षेत्रामध्ये स्थित, रिबिरा डी पेना अशी एक अशी नगरपालिका आहे जी उत्तरेत जास्त लांडग्यांसह एकाग्र असलेल्या भागात पर्यावरणीय कॉरिडॉरप्रमाणे काम करू शकते. दक्षिणेकडील एकाग्रता.

मी माझ्या जीवशास्त्र अभ्यासक्रमाच्या दरम्यान जीआयएस सॉफ्टवेअरचा वापर करण्यास सुरवात केली आणि बरेचदा मास्टर थीसिस दरम्यान मी त्या वेळी मुख्यतः मालकीचे सॉफ्टवेअर वापरले मी मास्टर पदवी संपल्यानंतर मालकीच्या सॉफ्टवेअरचा प्रवेश गमावला.

मी काही संशोधकांना जीआयएस वापरुन रिबिरा डे पेना मधील लांडग्यांसाठी इकोलॉजिकल कॉरिडोरचे मॉडेल तयार करण्यासाठी मदत करण्यासाठी संपर्क साधला आहे कारण त्यांनी या प्रकारच्या सॉफ्टवेअरवर कधीही काम केले नाही. कारण मी आधीच लिनक्स वापरत आहे. विंडोजऐवजी माझी पहिली समस्या कोणती सॉफ्टवेअर होती मग मी क्यूजीआयएस बद्दल ऐकले आणि मी प्रयत्न करण्याचा निर्णय घेतला, जरी मला आधीच माहित असलेल्या गोष्टींच्या तुलनेत हे अगदी सोपी आणि अपूर्ण वाटले. मी किती चुकलो हे मला पटकन समजले आणि मी QGIS ने दिलेल्या विश्लेषणात्मक क्षमतांनी खरोखर उत्साही झाले. , विशेषत: ग्रॅस एकत्रिकरणासह.

इकोलॉजिकल कॉरिडॉरचे मॉडेल तयार करण्यासाठी आम्ही जीआरएसएस प्लगिनसह क्यूजीआयएसचा उपयोग केला.पर्यावरणाच्या उपस्थितीच्या डेटासह आम्ही अनेक भौगोलिक माहिती वापरली, पर्यावरणीय कॉरिडॉरचे मॉडेल तयार केले.या प्रकरणात वापरल्या जाणार्‍या क्यूजीआयएस आणि ग्रॉस या दोहोंची काही कार्ये येथे आहेत. फक्त काही नावे देण्यासाठीः
- क्यूजीआयएस मधील प्लगइन प्रक्षेप: एक डिजिटल एलिव्हेशन मॉडेल तयार करण्यासाठी
- ग्रासमध्ये आर.पाणी: डीईएममधून पाण्याचे प्रवाह तयार करणे
- ग्रॅस मधील r.grow.distance: इनपुट लेयरमधील वैशिष्ट्यांकरिता अंतराचा रास्टर नकाशा थर व्युत्पन्न करते
- ग्रॅसमधील आर. क्लास: नकाशाच्या थरांचे पुन्हा वर्गीकरण करण्यासाठी
- r.slope.aspect.slope मधील ग्रास: DEM पासून उतार मोजण्यासाठी
- ग्रॅस मधील आर.माप कॅल्क्युलेटर: काही सोप्या नकाशा बीजगणिताची गणना करण्यासाठी
- ग्रॅस मधील आर कॉस्ट.कॉर्ड: एक इनपुट रास्टर नकाशावर वेगवेगळ्या भौगोलिक स्थानांदरम्यान फिरण्याची एकूण किंमत दर्शविणारा रास्टर नकाशा तयार करतो ज्याची सेल श्रेणी मूल्ये प्रतिनिधित्व करतात
- r.drain in GRASS: Traces a flow through an elevation model on a raster map — the one used to create the corridors

या कार्याद्वारे आम्हाला रिबिरा दे पेना नगरपालिकेत लांडग्यांसाठी संभाव्य पर्यावरणीय कॉरिडोरचा नकाशा प्राप्त झाला आहे.या प्रजातींसाठी संरक्षणाच्या उपाययोजना करतांना नगर परिषद तंत्रज्ञांनी या क्षेत्राचा विचार केला पाहिजे. या कॉरिडॉरला अत्यंत महत्त्व आहे कारण ते कनेक्ट होऊ शकतात दक्षिणेकडील विला रियल मधील नाजूक लांडगा पॅक-गेरेस आणि स्पेनमधील दक्षिणेकडील उत्तरेकडील देशांसोबत सतत चालू आहे. लहान गावे, शहरे आणि रस्ते यासारख्या मानवी वसाहती ओलांडणार्‍या त्या कॉरिडोरला विशेष महत्त्व आहे. लांडगा संवर्धनासाठी या भागांना गंभीर मानले पाहिजे आणि या प्रजातीतील मानवी प्रभाव कमी करण्यासाठी उपाययोजना लागू केल्या पाहिजेत.

<figure>
<img src="../images/portugal_ribeira2.png" class="align-right" style="width:100.0%" alt="portugal_ribeira2.png" />
<figcaption>Ecological corridors and critical conservation areas for wolves in northern Portugal.</figcaption>
</figure>

## निष्कर्ष
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## लेखक
<figure>
<img src="../images/portugal_ribeiraaut.png" class="align-left" height="200" alt="portugal_ribeiraaut.png" />
<figcaption>Monica Almeida</figcaption>
</figure>

या लेखाचे योगदान मोनिका अल्मेडा यांनी जुलै 2012 मध्ये केले होते. पोर्तुगाल मधील लांडगाच्या संवर्धनात एका स्वयंसेवी संस्थेत काम करणारे ती संवर्धन जीवशास्त्रज्ञ आहेत.

{{<content-end >}}
