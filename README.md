# Smart-Infotainment-System
Building a smart infotainment system with enhanced object detection for road safety

YOLO V9 Integration: Leverages the latest YOLO V9 model for high-performance, real-time object detection and multi-class classification.
Custom Dataset: Utilizes a bespoke dataset prepared and annotated using Roboflow, ensuring high accuracy and adaptability.
Real-Time Alerts: Provides voice alerts using natural language processing (NLP) and visual warnings through computer vision.
Edge Computing: Deployed on a Raspberry Pi, ensuring efficient, low-latency performance without reliance on cloud processing.
Seamless Integration: Designed to integrate smoothly with existing car infotainment systems via APIs and middleware.


YOLO V9 :-

YOLOv9 marks a significant advancement in real-time object detection, introducing groundbreaking techniques such as Programmable Gradient Information (PGI) and the Generalized Efficient Layer Aggregation Network (GELAN). This model demonstrates remarkable improvements in efficiency, accuracy, and adaptability.

It is trained on our custom dataset using roboflow.
![Screenshot (462)](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/aa31d246-466a-48bd-8d10-21c432af7e42)

Annotate each image-
![Screenshot (463)](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/b8e999a4-fbc0-4080-900f-4b128dfd880a)

YOLOv9's advancements are deeply rooted in addressing the challenges posed by information loss in deep neural networks. The Information Bottleneck Principle and the innovative use of Reversible Functions are central to its design, ensuring YOLOv9 maintains high efficiency and accuracy.
The Information Bottleneck Principle reveals a fundamental challenge in deep learning: as data passes through successive layers of a network, the potential for information loss increases. This phenomenon is mathematically represented as:

I(X, X) >= I(X, f_theta(X)) >= I(X, g_phi(f_theta(X)))

where I denotes mutual information, and f and g represent transformation functions with parameters theta and phi, respectively. YOLOv9 counters this challenge by implementing Programmable Gradient Information (PGI), which aids in preserving essential data across the network's depth, ensuring more reliable gradient generation and, consequently, better model convergence and performance.


the YOLOv9 series offers a range of models, each optimized for high-performance Object Detection. These models cater to varying computational needs and accuracy requirements, making them versatile for a wide array of applications.

![Screenshot (464)](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/e4524182-9b61-41d8-a92c-09062633e2fe)

The python snippets will be given on the folder top , which we built to detect our custom dataset using ultralytics inbuilt python module.

On training out custom model with epoch of 30 , over 11+ classes and nearly 1k images with batch of close to 10 and configuring the weights upto 0.5 , we pretty much ended up training an accurate model , with teh results bar shown below.
![Confidence curve](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/2becb82d-5559-4b40-95a6-d0a68dec2ef0)
![Confusion Matrix](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/68ebe3f4-158d-4b2f-a822-6bba6f1d149e)
![Percision-Confidence](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/5aa84a7f-fbcc-4370-ace7-07d8b005583e)
![Recall curve](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/23749d5a-8ea3-4f24-81f8-ebc6a50c0718)

![Normalised CNF](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/319a6662-d894-4bfb-84ec-780cb8637e49)
![Recall-Confidence](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/541360f5-23ad-40e8-aab9-95d0ddc608a5)
![Results](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/14e52f46-5a95-4a2b-a264-c2f0a764ebb7)


Our custom data set had various advantage over the pretrained YoloV9 MS COCO Dataset as ours could fit onto the indian Road conditions.

by even detecting Auto's XD!
![Screenshot (461)](https://github.com/nachiadhi/Smart-Infotainment-System/assets/127410673/9aba029c-72f0-460c-aa10-b932c320a948)

once finished training our ml model , next was to implement onto our hardware computer / (Raspberry Pi 5 )


