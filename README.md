<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This is a Python app for keeping track of elapsed time. This app also allows the user to input a time to start the stopwatch from, which most other stopwatches do not allow.

### Built With
* [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites
1. Verify python has been installed. To do this use the following command in the command prompt:
```bash
python -V
```
* If Python is installed, an output should be returned that is similar to: `Python 3.8.6 `
* If a Python version is not installed, it can be found at the [Python Downloads Page](https://www.python.org/downloads/)

2. Install PySimpleGUI
```bash
pip3 install pysimplegui
```

### Installation
Clone this repository to your desired folder.
```bash
git clone https://github.com/ltoleary3/Stopwatch-App.git
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
In folder where app is downloaded:
```bash
python stopwatch.py
```

In first window, you can enter a time that has previously elapsed or where you would like the stop watch to start from. This is useful in cases where you need to completely close the app, but would like to resume the timer from a set point.

_Note: If this field is left blank the timer will start at 0:00:00. In addition, every character that is not a digit (0-9) or colon (:) will be removed. If the input can't be parsed, the timer will start at 0:00:00._

To start timer, simply click on the 'Start' button.

Once the timer has been started and while the timer is running, this button will become 'Pause'. Clicking this will stop the timer while ocontinuing to display the elapsed time. It will also convert the 'Pause' button to 'Resume' which will allow the timer to run again from where the time displayed.

The 'Reset' button will stop the timer and clear the elapsed time, returning the user to the orginial display when the app is started.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License
Distributed under the [MIT License](https://choosealicense.com/licenses/mit/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact
Logan O'Leary - [Twitter](https://twitter.com/LoganTOleary) - Email: logantoleary.business@gmail.com

Project Link: [https://github.com/ltoleary3/Stopwatch-App](https://github.com/ltoleary3/Stopwatch-App)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[issues-shield]: https://img.shields.io/badge/ISSUES-open-yellow
[issues-url]: https://github.com/ltoleary3/Stopwatch-App/issues?q=is%3Aissue+is%3Aopen+
[license-shield]: https://img.shields.io/badge/LICENSE-MIT-green
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/LINKEDIN-LoganOLeary-blue
[linkedin-url]: https://www.linkedin.com/in/logantoleary/
