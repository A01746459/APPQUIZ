# APPQUIZ

<h2> Team members </h2>
<div> * Jeovani Hernandez Bastida | A01749164 </div>
<div> * José Miguel Garcia Gurtubay Moreno | A01373750 </div>
<div> * Sebastian Burgos Alanís | A01746459 </div>
<div> * Sandra Ximena Téllez Olvera | A01752142 </div>

## General overview

The APPQUIZ is a web application that allows users to participate in a quizz by answering questions related to software architecture, design patterns and SOLID principles and keeping track of their scores. Users can also view the leaderboard to see the top scorers.

## Functionality Video
https://drive.google.com/drive/folders/1wzEHMk0qw1roMSKuKUkuK6H3rikv-YtH?usp=sharing

## Installation (Locally)

1. Clone the repository:
```
git clone https://github.com/A01746459/APPQUIZ.git
```  

2. Navigate to the project directory:
```
cd ...\AppQuiz`
```

![instrucciones](https://github.com/A01746459/APPQUIZ/assets/65176372/68e3774b-d5f3-4765-9739-c720208957c8)

3. Activate a virtual environment:
```
.\Scripts\activate
```

![instrucciones1](https://github.com/A01746459/APPQUIZ/assets/65176372/5d4481ad-940c-46dd-914d-0a9235ce13e8)

4. Navigate to Aplicativo
```
cd Aplicativo
```

5. Start the development server:
```
python .\manage.py runserver
```    

![instrucciones2](https://github.com/A01746459/APPQUIZ/assets/65176372/5b17cfab-56af-4dc8-8059-ddcf4e2a9d80)

6. Login to the server
```  
https://127.0.0.1:8000
```  

## Diagram(s) of the system and its constituent parts.

![DiagramaAppQuiz](https://github.com/A01746459/APPQUIZ/assets/65176372/e4155a87-f55b-4a80-b301-ab72e0e4c5f7)

## Design Pattern Review
During the development of the quiz app, we consider that, the best Design pattern that we can use is the Model View Template, here are the reasons:

- The Model will be in charge of the management of the questions, answers and users.
- The View will be the interface in which the user data is presented, there, the questions and the answers will be collected.
- The Template will manage the events, like the choosing of answers or the presentation of the next question.

## The flow of the app using the MVT pattern would be the following:

- The user requests a question through a specific URL.
- Django maps that URL to a corresponding view.
- The view retrieves the question and answer options from the model.
- The view renders a template with the question and answer options.
- The user selects a response and sends the request to the server.
- Django maps that request to a corresponding view.
- The view processes the user's response, checks its validity, and updates the data as needed.
- The view renders a template with the question results.
- The user sees the results in the browser.

![MVT](https://github.com/A01746459/APPQUIZ/assets/65176372/2f4d2c4c-8d23-4efe-b890-22cc9aec91fe)

## Feedback 
As a group, we all worked hand by hand. We had a little of problems at the end, but we managed to carry on and we delivered the work in place and time. 

References
- programadorY. (2021, March 30). Aprende a crear una App de Quiz con Django. Introducción [Video file]. Retrieved from https://www.youtube.com/watch?v=3OJxDX14A3A&list=PLZyaZrHcg9P7RWc5IotQNwQfVZVAnpySe  
- freeCodeCamp.org. (2023, March 22). Django Project – Code a CRM App Tutorial [video file]. Retrieved from https://www.youtube.com/watch?v=t10QcFx7d5k
- Martin, R. C. (2003). The Principles of OOD (SOLID). Retrieved from https://web.archive.org/web/20190517172845/https://web.archive.org/web/20190517172845/http://www.butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod       
