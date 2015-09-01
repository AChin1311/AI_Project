So, where are the Ads?
====

This is an Aritificial Intelligence course project, which significantly improve the quality of results when searching Chinese hashtags on Instagram. We also developed a web application for users to easily create a website which filtering the spam posts when searching Chinese tags.

## Motivation

Instagram is an online mobile photo-sharing, video-sharing and social networking service, which rapidly gained popularity, with over 300 million as of December 2014. One of the features in Instagram is that users can add hashtags on their posts. Using specific tags help users connect with other like-minded people on Instagram. 

For example, when searching #cat on Instagram, users can explore a variety of photos related to cats. Therefore, we wonder how well do the Chinese hashtags perform on Instagram. We searched for posts with hashtag #台灣. Out of our expectation, instead of getting beautiful scenes in Taiwan or anything related, the results were full of spamming and advertising posts! What a bad user-experience. Thus, we decided to improve the quality of results when searching for Chinese hashtags through recognizing the spam posts with machine learning techniques. 

## Installation

1. Get your access code on Instagram, please see the tutorial (http://stackoverflow.com/questions/16496511/how-to-get-an-instagram-access-token)
2. Create a new file ```./code/config.py```, and add a line of code ```token = "[your-token]"```
2. Download libsvm-3.20 (https://github.com/cjlin1/libsvm/releases) and unzip to the directory **./code/mltools**
2. Change directory to ```./code/mltools/libsvm-3.20/python``` and type ```make```
3. Type ```python server.py ../model/spamtag_ver3.model ../model/spamtag_ver3.model.range 9999```
4. Then the service will run on the 9999 port, visit [http://localhost:9999](http://localhost:9999)
5. Succeed! now you can input any hashtags to the top-right search bar!

If you are interesting to our technical details, please check our poster.

## Reference

_F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay, “Scikit-learn: Machine learning in Python,” Journal of Machine Learning Research, vol. 12, pp. 2825–2830, 2011._

_R.-E. Fan, K.-W. Chang, C.-J. Hsieh, X.-R. Wang, and C.-J. Lin, “LIBLINEAR: A library for large linear classification,” Journal of Machine Learning Research, vol. 9, pp. 1871–1874, 2008._

_C.-C. Chang and C.-J. Lin, “LIBSVM: A library for support vector machines,” ACM Transactions on Intelligent Systems and Technology, vol. 2, pp. 27:1–27:27, 2011. Software available at http://www.csie.ntu.edu.tw/~cjlin/libsvm._

_Y.-W. Chen and C.-J. Lin, “Combining SVMs with various feature selection strategies,” in Feature extraction, foundations and applications (I. Guyon, S. Gunn, M. Nikravesh, and L. Zadeh, eds.), Springer, 2006._

_B.-Y. Chu, C.-H. Ho, C.-H. Tsai, C.-Y. Lin, and C.-J. Lin, “Warm start for parameter selection of linear classifiers,” 2015._
