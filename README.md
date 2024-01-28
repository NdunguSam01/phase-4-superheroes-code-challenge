# Flask Code Challenge - Superheroes

## Project Description

This project is a Flask based application that creates an API tracker for tracking heroes using Flask and SQLAlchemy for the back end and React for the front end.

## Project Pre-requisites

To successully run this project, the following software(s) need to be installed in your machine:

1. **Python** - You can download it from their [official site](https://www.python.org/downloads/).
2. **Pipenv** - This is a Python virtual environment management tool that automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile. You can download it from their [official site](https://pypi.org/project/pipenv/).

## Project Setup Instructions

In order to successfully view the output of this project, create a new directory where you want to store the project files, navigate into it and follow the instructions below:

1. **Cloning**- clone the repository by typing the following command into your terminal:

    ```
    git clone https://github.com/NdunguSam01/phase-4-superheroes-code-challenge.git 
    ```

    Optionally, you can download the zipped file by clicking the green Code button then selecting the "Download ZIP" option.

2. **Installing dependencies** - since this project needs various dependencies to run, type the following command in your terminal:

    ```
    pipenv install
    ```

    After this operation is completed, run the following command to enter into the virtual environment:

    ```
    pipenv shell
    ```

3. **Creating the database** - once you have successfully cloned the project, navigate into the code-challenge folder then into the app folder

    ```
    cd code-challenge/app 
    ```

4. **Create the database** - since the project's database migration has already been done, run the following command to create an instance of the database

    ```
    flask db upgrade 
    ```

5. **Seed the database** - to successfully view the results, run the seed file  which will populate the database with data

    ```
    python3 seed.py
    ```

6. **Start the Flask API** - to start the Flask API, run the app.py file

    ```
    python3 app.py
    ```

Once the server runs, you can view the results via [http://127.0.0.1:5555/](http://127.0.0.1:5555/)

## Viewing results
The project has the following endpoints:

1. http://127.0.0.1:5555/heroes - retrieves the details for all heroes 
2. http://127.0.0.1:5555/heroes/:id - retrieves  a specific hero by their id
3. http://127.0.0.1:5555/powers - retrieves all the powers in the database
4. http://127.0.0.1:5555/powers/:id - retrieves details of a power based on the passed in id
5. http://127.0.0.1:5555/hero_powers - adds a new hero-power into the database. It accepts a strength, hero_id and power_id as arguments

Navigate into the links above to view the results.

**NB: Remember to pass in an integer  value for :id when accessing a single resource. The characters ':' should not be included in the URL.**

## Author

[Samuel Muigai](https://github.com/NdunguSam01)

## License

MIT License

Copyright &copy; 2024 Samuel Muigai

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.