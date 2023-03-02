National Parks 
------

<img width="500" height="300" alt="National Parks Logo" src="https://res.cloudinary.com/decu5fbul/image/upload/v1677785031/National%20Parks/np_logo2_qedi0t.png">

### Application Overview

National parks are full of wonder, adventure, solitude, and freedom.  From the novice hiker to the seasoned outdoorsman, national parks are meant to be explored.  National Parks is a web application designed to make the parks more accessible to all types of explorers and provide resources for getting to know the parks and planning your next great adventure.  The app covers all things national parks including events, visitor blogs, campgrounds, wildlife and more that you can experience at each park.  Join our app, and get exploring!

This full stack application was created as part of a group learning project and consisted of three Agile sprints.  Our learning goals were to: 
- **Sprint #1**
  - Collaboratively plan out an application through the use of brainstorming, wireframing, and ERD creation
  - Utilize a Github project board to create issues and manage work across the team
  - Design and build a SQLite database and seed it with data for development purposes 
  - Create a RESTful API with Python to handle requests from the National Parks Client
  - Maintain a robust code base through the use of git/Github source control, detailed pull requests, and code reviews
- **Sprint #2**
  - Build out the essential components of the client using the React framework
  - This included creation of the landing page, nav bar, user login and registration, blog page, and individual park pages
- **Sprint #3** 
  - Redesign the API utilizing the Django REST framework 
  - Deepen understanding of the Django object relation mapping (ORM) API and user authorization process
  - Refactor the client to be compatible with the Django API
  - Upgrade the client to have a responsive design using the Bootstrap CSS framework
  - Enhance the client through the addition of features and functionality initially pegged as stretch goals

### Features

  
### User Experience

#### Login to app
------
![](src/media/HouseHub_Login.gif)

#### Add a task
------
![](src/media/HouseHub_Add_a_Task.gif)

#### Create a work order
------
![](src/media/HouseHub_Create_a_Work_Order.gif)

### Technologies Used

<img alt="Javascript" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"><img alt="React" src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"><img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"><img alt="CSS" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"><img alt="JSON" src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white"><img alt="GIT" src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white"><img alt="Github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"><img alt="VScode" src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"><img alt="Miro" src="https://img.shields.io/badge/Miro-F7C922?style=for-the-badge&logo=Miro&logoColor=050036"><img alt="" src="">

HTML, Javascript (React Framework), JSON server and CSS were used to build and style this application.  In the planning stages, I used DBDiagram to create an entity relationship diagram and Miro to create a wireframe.  Both documents helped with my solution design and were referenced throughout my work building out this app.

* [HouseHub ERD](https://dbdiagram.io/d/637cf58cc9abfc61117480ed)

* [HouseHub Wireframe](https://miro.com/app/board/uXjVP_UeasE=/?share_link_id=143430286106)
                
### Roadmap
* Filter dropdowns on task, contractor and work order pages
* Additional home detail fields that allow for lower level detail tracking (i.e. serial number, manufacturer, color, etc.) 
*  Auto-formatting of phone numbers 
*  Quote and invoice upload on work orders 

### Running the Application

Navigate to your workspace directory. 

Run the following command in terminal:

```
git clone git@github.com:vanessaspear/house-hub.git
cd house-hub
npm install
npm start
```

This runs the app in development mode.  Open [http://localhost:3000](http://localhost:3000) to view it in your browser. 
 
Navigate back to your workspace directory in terminal to download the database.

Run the following command in terminal:

```
git clone git@github.com:vanessaspear/house-hub-api.git
cd house-hub-api
json-server database.json -p 8088 -w
```

You should now be able to login to the application. 

To demo the app, login in with the following email address: **wthorneloe1@usa.gov**

Author
------
Created by Vanessa Spear 

[<img alt="Github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">](https://github.com/vanessaspear)[<img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">](https://www.linkedin.com/in/vanessavspear/)
