{
  "title": "The War of Autonomous Driving: Computer Vision and LiDAR",
  "authors": [
    "Hanlin Ma"
  ],
  "year": 2022,
  "venue": "Chinese Social Sciences Today",
  "type": "article",
  "publication_section": "articles",
  "published_in_chinese": true,
  "pdf": "/files/publications/the-war-of-autonomous-driving.pdf",
  "abstract": "This article analyzes the technical and conceptual debate between computer vision and LiDAR in the development of autonomous driving systems. It argues that the disagreement is not merely about engineering preference, but about competing assumptions concerning perception, safety, and the future trajectory of intelligent mobility.",
  "tags": [
    "ai",
    "philosophy-of-technology"
  ]
}

This English version is translated from the original Chinese publication.

## English Translation

In recent years, a "war of autonomous driving" has been unfolding in the field of intelligent vehicles. On April 22, 2019, Elon Reeve Musk declared at Tesla's Autonomy Day event that using LiDAR was futile and that anyone relying on it was bound to fail. At the time, aside from Tesla's commitment to computer vision, most autonomous-driving developers treated LiDAR as the core sensor for self-driving vehicles and as a key device for building machine perception. Musk's remarks therefore caused a major response in the industry and helped bring the conflict between computer vision and LiDAR to the center of debate.

LiDAR matters because it can provide depth information. Its basic principle is to emit laser beams and receive reflected signals in order to construct a three-dimensional image of the surrounding environment. It also has obvious shortcomings: it struggles in extreme weather, cannot directly identify color-image information, and has difficulty capturing certain finer details. The computer-vision camp dislikes LiDAR mainly for two reasons. First, a LiDAR-centered route may rely heavily on high-definition maps, and the uncertainty surrounding those maps creates not only technical challenges but also large engineering burdens in production and maintenance. Second, LiDAR remains expensive, while image sensors are cheaper. Layered imaging, simulated LiDAR, and stereo-vision sensors may all be used to estimate depth and thereby replace LiDAR, but these technologies are still developing.

Advocates of computer vision argue that autonomous driving should rid itself of LiDAR as an unnecessary technology or device. Their reasoning is that the sensing system of an intelligent vehicle should imitate human beings as far as possible, and human beings complete the task of driving with only two eyes. On this view, intelligent vehicles should likewise approach human capability through computer vision. Some therefore believe that, in the long run, computer vision will be the ultimate answer for autonomous driving. It is worth noting, however, that many people who hold this view come from machine learning, especially deep learning, and their confidence in computer vision is rooted in confidence in deep learning itself. In other words, they take deep learning to be the future of fully autonomous driving. Yet judging from current industry practice beyond Tesla, computer vision has not won universal acceptance. Deep learning, moreover, can be applied not only to computer vision, especially for depth processing, but also to the integration of data from many sensors, including LiDAR, into a kind of unified perceptual synthesis that supports inference and prediction.

Sacha Arnoud has argued that the more sensors the better. At present, it still seems that once autonomous driving aims above the L4 level, LiDAR is difficult to replace because computer vision still cannot reliably detect depth. At the same time, the rapid development of related industries has quickly reduced the cost and size of LiDAR, which weakens the position of the computer-vision camp. Because radio technology and LiDAR technology are historically related, powerful later entrants such as Huawei may also have the opportunity to develop better and cheaper LiDAR systems. Even so, this war of autonomous driving is far from over, and premature conclusions should be avoided. Data is the lifeblood of deep-learning-based computer vision, and when the market recognizes autonomous-driving products from the computer-vision camp, those firms gain the conditions to collect large amounts of vision-based data. This gives them a technical foundation for continuing along the same path. In addition, intervention by legal and political factors will make the conflict still more complex.

In my view, deep learning is a technical path that depends on "big data," whereas human vision and human reasoning form an intelligent pattern based on "small data." In an important sense, the technical path of computer vision has never completely abandoned other sensors. Moreover, the high degree of integration between human vision and the rest of human cognition is something current mainstream AI design still cannot simulate. Driving is a comprehensive cognitive process. Even if a system were to approach human beings ever more closely in visual terms, that alone would not amount to autonomous driving in the full sense. Even if developers succeeded in building systems with enough sensors, including LiDAR or simulated LiDAR, this still would not guarantee L5 autonomous driving, much less anything beyond L5. Fully autonomous driving requires not only adequate perception but also very advanced intelligent reasoning. To reach or exceed the level of safety required for superhuman driving, developers would need major breakthroughs on that second front as well.
