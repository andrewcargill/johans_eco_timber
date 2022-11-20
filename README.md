# Sustainable Timber Co. 

![alt text](static/images/about_hero.jpg)

It's time to really celebrate and support businesses that have the environment at the heart of their products. Sustainable Timber Co. is owned and run by Johan Johansson, a highly creative person with a small forest and sawmill.

For Johan the nature is important and every tree has a story. Based in the north of Swedish, his method of forestry ensures that the nature remains unharmed and that every tree removed is removed for a good reason. As a result Johan only removes a small number of trees each year and the price of those trees must be of a premium. 

Johan is able to custom mill the trees to exactly what his customers require. Customers like instrument builders, furniture makers and timber-frame house renovators. 

Johan is part of the team. Solving a problem for his customers. What better way to do this than a custom built online enquiry system that allows users to specifically detail what they need and when they need it. Giving Johan the information he needs to really offer his customers a unique and premium experience.  

<details><summary><font size="4">Project Presentation</font></summary>

### Presentation of the project
Custom Timber Co. is a small company up in the north of Sweden that specialise in custom milled timber, owned by Johan, a guy who is passionate about the nature and the environment. This website is connecting Johan to his customers and helping communication in a modern and effective way.

### Overview of the development journey
Before I begin documenting this projects development I wanted to highlight that this project really did help me understand the effectiveness of 'agile' and that my original planning proposed the creation of a two database system  - but early into development I understood that this was not going to work and so I privotted the project and created a really great solution. I will document this later within my documentation. But I felt it important to make the reader away. 
</details>


<details><summary><font size="4">Design Thinking</font></summary>

### The company
This is based on a real-life company in the North of Sweden. For these small sawmills it is currently hard for them to connect with customers, without having a custom made website and backend. Often enquires and communications are done via Facebook or some-kind of primitive local online market place. 

### Customer Interviews
![alt text](readme_media/interview1.png)
![alt text](readme_media/interview2.png)
![alt text](readme_media/interview3.png)
I spoke with several people who worked made custom wood products, that I know would need to buy timber. 


### Research
Brain Storm 1 - General ideas for the website
![alt text](readme_media/brain_storm.png)
Brain Storm 2 - Focusing in on viable ideas
![alt text](readme_media/brain_storm2.png)
The projects - Persona
![alt text](readme_media/research_persona.png)

Much research was carried out. I visited the sawmill and spoke with the owner about his needs and desires.

### Video Proposal
Here is my mock proposal video, which I used to shape up the project before starting development. 

### Wireframes
My original wireframes for the project look a little different to the finished project. These evolved as the project progressed. 

### Planning & Design
My original plan was to use two databases but this was later simplified to one database linked to the users primary key. 

</details>

<details><summary><font size="4">Agile</font></summary>

<details><summary>User Stories
</summary>
I generated over 100 user stories in developing this project. I made use of the 'project' feature within GitHub to manage the ordering and completion. 
</details>

<details><summary>Story Points & Sprints
</summary>
My allocation and valuing of story points moved a little as the project progressed. I completed my first sprint and re-assessed the value of 1 story point - After the first week of development I was confident on the value of one story point. For me this was a User Story that I knew how to complete and required little background research. 

Sprint lengths changed depending on my work/ study hours for that day or week of production. This would be much easier with a standard 40hr week, but I did feel that it was useful to apply sprints to my work even when working alone and studying as I do, as it helped me set goals for sections of the projects development.
</details>



<details><summary>Epics into User Stories
</summary>
I have two examples of where I have set epics and then broken them down into User Stories. 
- Final design
- Documentation
</details>



<details><summary>Timeline - Development
</summary>
I have put together a small time line to document the progress of the project from start to end. This highlights my sprints and allocation of story points etc.
</details>

</details>

<details><summary><font size="4">Features</font></summary>

### Existing Features

<details><summary>Navigation</summary>

- Responsive design
- Displays custom menu for logged in user
- Display custom menu for Admin (Superuser)
- Displays status of user login - logged out

</details>

<details><summary>Website</summary>

- Responsive design
- Simple information
- Clearly displaying 'Johan' to build customer trust

</details>

<details><summary>Enquiry System</summary>

- Responsive design
- User can create an enquiry
- User can edit an enquiry
- User can submit an enquiry
- User can delete an enquiry
- Admin can update the status to 'emailed'. This will reflect in users view

</details>

### Future Features

</details>

<details><summary><font size="4">Testing</font></summary>
<details><summary>Manual Testing 
</summary>

| Page        | Description           | Result  |
| ------------- |-------------| -----|
| Index.html    | About button | Pass |
|      | Responsive Design - Mobile > Large      |   Pass |
|      | Hello, I'm Johan Link      |   Pass |
|  | True Sustainable Forestry Link      |Pass |
||How I can help... Link|Pass|
||Take only the trees... Link|Pass|
||That creatuve... link|Pass|
|About|Responsive design - Mobile > Large|Pass|
||Link test|Pass|
|Forest|Responsive Design - Mobile > Large|Pass|
||Link test|Pass|
|Customer Timber|Responsive Design - Mobile > Large|Pass|
||Link test|Pass|
|Login|Log in with Username & Password|Pass|
||Login with incorrect details (help text)|Pass|
||Link to 'sign up' test |Pass|
||Successful login - User to 'quote_list' with username displayed |Pass|
||Successful login - Admin to 'quote_list' with username displayed |Pass|
|Sign up| Sign up with correct information |Pass|
||Sign up with incorrect info (help text)|Pass|
||Test 'sign in' link|Pass|
|Enquiry (list view)|Responsive Design - Mobile > Large|Pass|
||New enquiry button loads new enquiry form|Pass|
||Sign out button loads sign out confirmation view|Pass|
||(Unsubmitted) Delete button loads delete confirmation view|Pass|
||(Submitted) Delete button loads delete confirmation view|Pass|
||(Email sent) Delete button loads delete confirmation view|Pass|
||Scrolling for many items|Pass|
|New Enquiry form|Responsive Design - Mobile > Large|Pass|
||Completed form - submit button - saves and loads list view|Pass|
||Uncompleted form - submit button - help text shown|Pass|
||Cancel button - User returned to list view|Pass|
||Datepicker - Loads when clicked|Pass|
||Number fields - Only except numbers|Pass|
||Comment field allows for large string|Pass|
|Submit form view|Responsive Design - Mobile > Large|Pass|
||Displayed details match the record being submitted|Pass|
||Submit button - changes status of enquiry and loads list view|Pass|
||Cancel button - Enquiry remains unsubmitted - loads list view|Pass|
|Delete view|Responsive Design - Mobile > Large|Pass|
||Delete button - Loads list view and removes the enquiry|Pass|
||Cancel button - Loads list view and enquiry remains in list|Pass|
|Edit Enquiry|Responsive Design - Mobile > Large|Pass|
||Save changes button updates enquiry|Pass|
||Cancel button returns user to list view|Pass|
||Incorrect changes - Help text shown|Pass|
|Alert Box|Alert shown after enquiry saved|Pass|
||Alert shown after enquiry edited|Pass|
||Alert shown after enquiry submitted|Pass|
||Alert shown after user logs out|Pass|
|User status|Not shown when user is not logged in|Pass|
||Displays users name when logged in|Pass|
||Confirms user has logged out - after logout|Pass|
|Navigation|Responsive Design - Mobile > Large|Pass|
||Home links to index.html|Pass|
||About links to about.html|Pass|
||Out forest links to outforest.html|Pass|
||Custom timber links to about_enquiry_system.html|Pass|
||Login links to accounts/login/|Pass|
||Sign up links to /accounts/signup/|Pass|
||User Logged in - Enquires links to quote_list.html|Pass|
||User logged in - New Enquiry links to new_enquiry.html|Pass|
||User logged in - Log out links to accounts/logout/|Pass|
||Admin logged in -Admin control panel links to /admin |Pass|
||Admin logged in - Log out links to accounts/logout/|Pass|
|Admin view|Admin changes status to emailed - Updates list view|Pass|

</details>

<details><summary>Automated Testing
</summary>
Xxx
</details>

</details>


<details><summary><font size="4">Bugs</font></summary>

### Solved

<details><summary>Bootstrap & Materialize
</summary>
I had zero experience on these and as both were used in the walkthroughs I thought they were equals. I went with Materialise. This backfired when I was trying to work out forms as I was informed by a tutor that Materialise was seen as very dated and that I would experience problems with Django should I choice to continue working with it. 

As this project involves many elements I found that I didn’t really have the time to focus and learn the true powers of Bootstrap. For this project it is used on a basic level.
</details>
<details><summary>Power of Agile - A change of direction
</summary>
I needed to change direction on the enquiry system implementation. My original plan was to allow the user to create an enquiry, add a number of items to the enquiry and then submit the enquiry. At the stage where I had the database models installed and was trying to solve the problem of including items within the enquiry I realised that this was maybe a little ambitious for this project. 

I decided to simplify the idea into one database and enable the user to create an enquiry and then submit the enquiry. The system would allow the user to create and submit any number of enquires. 
</details>

<details><summary>Deployment
</summary>
I spent 3 hours working with Rebecca (Tutor) to help me get the site live. 
</details>

### Unsolved

<details><summary>Styling of Sign up
</summary>
I just ran out of time!
</details>

<details><summary>Selecting deadline date
</summary>
There should be an error if a user selects a date which is in the past. I looked into solving this but I felt I just didn't have the time to do it. 
</details>

<details><summary>Another
</summary>
Xxx
</details>

</details>

<details><summary><font size="4">Deployment</font></summary>

### Deploying to Heroku
### Database setup
### Cloudinary

</details>

<details><summary><font size="4">Credit & Acknowledgements</font></summary>

### Credits
### Acknowledgements
</details>


