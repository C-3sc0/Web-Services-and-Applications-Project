# Web-Services-and-Applications-Project

Author: Francesco Troja

This repository serves as a key resource for the project of the **HDip in Computing within ATU University's Data Analytics program**, specifically for the **Web Services and Application** module. It includes a `Flask server` file named `server.py`, along with two folders named `static` and `templates`. These folders contain **images**, **CSS styling**, and all the **HTML pages** essential for the project.

## Web Hosting Repository Link

For hosting the website, the `Pythonanywhere hosting web platform` was utilized. On this platform, both the *Flask server* and the *database* were incorporated. This setup ensures that whenever a movie or TV show is added to the wishlist, the corresponding data is also stored in a MySQL database. 

The website can be accessed via the following link:

<p align="center">
  <a href="https://c3sc093.pythonanywhere.com/">Create your own Wishlist</a>
</p>

Additionally, a section will be provided below to clarify the functionality of the website.

## Website Overview and Features

The **website's goal** is to provide a *wishlist* page where users can seamlessly **add**, **update**, or **remove** their *favorite* movies or TV shows after selecting them from the movie and TV show database.

For *retrieving movie and TV show information*, an external `API` from the **[The Movie Database (TMDB) website](https://developer.themoviedb.org/docs/getting-started)** was chosen. The decision to utilize this API was primarily influenced by its **accessibility**, given that it was freely accessible and only required an `API Key` for full access to retrieve all pertinent information. Additionally, the API was selected for its comprehensive range of *valuable data*, encompassing various details such as *movie* and *TV show* *titles*, *overviews*, *release dates*, *ratings*, *genres*, *cast*, *posters*, and more. This breadth of information made it an ideal choice for populating the movie and TV show database on the website.


The website utilized two distinct pages, namely `movie.html` and `tv-show.html`, to initially **fetch** all the information from the API and display the *poster*, *title*, *rating*, and *overview* for each movie or TV show. Within the overview information, a **button** was incorporated to allow users to *add their favorite movie or TV show to their wishlist*. Upon *adding* a movie or TV show to the wishlist, the *selected item's ID, title, and poster information* will be automatically appended to the wishlist table. In cases where the movie or TV show is already present in the wishlist, an alert would prompt the user to select a different item.

The website provides two functions for managing items in the wishlist: **deleting** and **updating** movies or TV shows. If a user accidentally adds an item they didn't want, they can *quickly delete* it by clicking the delete button next to the respective item in the wishlist table. Alternatively, they can choose to *update* the mistakenly added movie or TV show with a new one. Upon clicking the "**Update Movie**" or "**Update TV Show**" button, the user will be prompted to enter the title or part of the title for the new item. Once selected and submitted, the new information will replace the existing item in the wishlist.

## How to download the Repository

Access the provided link: [Web-Services-and-Applications-Project](https://github.com/C-3sc0/Web-Services-and-Applications-Project) and select the `<> Code` button. There are two options for accessing the repository:

- Download it as a `ZIP file`;
- Clone the repository using the provided `HTTPS link` and integrate it into your local machine.

## Repository's Content

- A file named **README.md** file;
- The [`server.py`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/blob/main/server.py) file, containing the Flask server;
- The [`static`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/tree/main/static) folder, containing a folder with the images used in the website and the `CSS` style document.
- The [`templates`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/tree/main/templates) folder, containing all the `HTML` files.

The HTML file comprises:

- [`project.html`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/blob/main/templates/project.html). This file serves as the landing page for the entire project. Here, users have two options to access information: they can either navigate using the navigation bar to access the other five pages, or they can use the three buttons located at the bottom of the page to directly access the movie and TV show database or the wishlist.
- [`about.html`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/blob/main/templates/about.html). This page solely displays the project requirements to the user and does not include any additional functionality.
- [`movie.html`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/blob/main/templates/movie.html). This page features the Movie Database fetched from the TMDB API.
- [`tv-show.html`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/blob/main/templates/tv-show.html). This page features the Tv show Database fetched from the TMDB API.
- [`wish-list.html`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/blob/main/templates/wish-list.html).This is the user wishlist, which initially appears empty when the user first accesses it. It will be populated once items are added.
- [`documentation.html`](https://github.com/C-3sc0/Web-Services-and-Applications-Project/blob/main/templates/documentation.html). Here, the user will find a comprehensive list of all the major references that have been utilized to complete the project.


## Technologies Used

The project utilizes **Python 3** as its primary technology stack. The official Python package can be obtained from the [Python website](https://www.python.org/downloads/) for download and installation. The utilization of Python 3 ensures compatibility with an extensive array of libraries and tools.
The libraries employed in the current codes include:

- Flask (The documentation can be found in the following link: [Flask](https://flask.palletsprojects.com/en/3.0.x/));
- MySQL Connector (The documentation can be found in the following link: [MySQL Connector](hhttps://dev.mysql.com/doc/connector-python/en/));

The majority of the required libraries are typically pre-installed in the Python environment. In cases where a library is not present, the `pip command``, serving as the Python package installer, can be employed. To facilitate the installation process, open the terminal and execute the following command:

```python
pip install library_name
```

It's important to substitute "library_name" with the actual name of the library intended for installation.