# Lipilok

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### A tool that offers mastery over the world of writing ✍🏻

<p align="center">
    <img src="assets/logo.webp" width="320" height="220">
</p>

# Lipilok

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### A tool that offers mastery over the world of writing ✍🏻

<p align="center">
    <img src="assets/logo.webp" width="320" height="220">
</p>

<hr>

# 🤔 Pre-requisites

- `python3`
- `pdm`

## 🐍 Python Version Support

This project is designed to be compatible with specific versions of Python for optimal performance and stability.

### Supported Python Version

- **Python>=3.10**

> ❗️ For the best experience and performance, it is recommended to use the version mentioned above.

Before diving into the project, ensure that you have the correct Python version installed. To check the version of Python you currently have, execute the following command in your terminal:

```bash
python --version
```

### 🐍 Installing Python 3.10 with `pyenv`

**Protip:** Managing multiple Python versions is a breeze with [pyenv](https://github.com/pyenv/pyenv). It allows you to seamlessly switch between different Python versions without the need to reinstall them.

If you haven't installed `pyenv` yet, follow their [official guide](https://github.com/pyenv/pyenv) to set it up.

Once you have `pyenv` ready, install the recommended Python version by running:

```bash
pyenv install 3.10
```

> When you navigate to this project's directory in the future, `pyenv` will automatically select the recommended Python version, thanks to the `.python-version` file in the project root.

# 📦 Setup

## Note: We use `.env` to define the download model, So create `.env` with respective model name from the table of models or Defaulf model will be selected as `MODEL="en"`

```env
MODEL="MODEL NAME"
```

### We currently support these models

<table>
  <tr>
    <th>Model</th>
    <th>Size</th>
  </tr>
  <tr>
    <td>en</td>
    <td>84M</td>
  </tr>
  <tr>
    <td>en_large</td>
    <td>284M</td>
  </tr>
  <tr>
    <td>hi</td>
    <td>75M</td>
  </tr>
  <tr>
    <td>hi_large</td>
    <td>374M</td>
  </tr>
</table>


## Local setup 🛠️ with Docker 🐳

<!--
- **Installing and running**:
  Before you begin, ensure you have docker installed. If not, refer to the [official documentation](https://docs.docker.com/engine/install/) to install docker.
  ```bash
  docker pull mrsunglasses/pastepy
  docker run -d -p 8080:8080 --name pastepyprod mrsunglasses/pastepy
  ```
  -->

- **Using docker-compose**:
  You can also use docker-compose to run the project locally by running the following command:
  <br>
  - **Clone the repository**:
  Get the project source code from GitHub:

  ```bash
  git clone https://github.com/BharatSahAIyak/spellcheck
  ```

  - **Navigate to the Project Directory**:

  ```bash
  cd spellcheck
  ```

  - **Run the project using docker-compose**:

  ```bash
  docker-compose up
  ```

## Local setup 🛠️ without Docker 🐳

### Setting Up the Project with PDM

[PDM (Python Development Master)](https://pdm.fming.dev/latest/) is utilized for dependency management in this project. To set up and run the project:

- **Installing PDM**:
  Before you begin, ensure you have PDM installed. If not, refer to the [official documentation](https://pdm.fming.dev/latest/) to install PDM.

- **Clone the Repository**:
  Get the project source code from GitHub:

  ```bash
  git clone https://github.com/BharatSahAIyak/spellcheck
  ```

- **Navigate to the Project Directory**:

  ```bash
  cd spellcheck
  ```

- **Install Dependencies**:
  Use PDM to install the project's dependencies:
  ```bash
  pdm install
  ```
* **Download models for spello**:
  Use PDM to run the project:
  ```bash
  pdm run download_model
  ```

* **Start the Project**:
  Use PDM to run the project:
  ```bash
  pdm run start
  ```
