<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Anomaly Detection Project</h1>
 Anomalous Score >= 3 (We Will be updating readme file soon!)

 
 
 
  <h2>Table of Contents</h2>
  <ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ul>
 
 
 
 
 
 

  <h2 id="introduction">Introduction</h2>
  <p>
    Anomaly detection plays a crucial role in identifying and mitigating potential security threats.
    This project focuses on detecting anomalies in user login behavior, which can help identify suspicious activities such as unauthorized access attempts or compromised user accounts.
    The project utilizes machine learning techniques, specifically XGBoost, to train an anomaly detection model based on a labeled dataset.
    The trained model can then be used to classify new login events as normal or anomalous based on their features.
  </p>

 
 
 
 
 
<h2 id="installation">Installation</h2>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/&lt;your-username&gt;/anomaly-detection.git
cd anomaly-detection
</code></pre>

<ol start="2">
  <li>Create and activate a virtual environment (optional but recommended):</li>
</ol>

<pre><code>python3 -m venv env
source env/bin/activate
</code></pre>

<ol start="3">
  <li>Install the required dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>
 
 <ol start="4">
 <li>
      Download the dataset:
      <p>
        The dataset used for training and testing the anomaly detection model should be placed in the <code>data</code> directory.
        Make sure to follow the appropriate data format and column structure.
      </p>
    </li>
  </ol>
 
 
 
 
 
 

<h2 id="usage">Usage</h2>
 
 
 
 
 

<h3>Data Preparation</h3>


  <li>Place your login data file (<code>Login_Data.csv</code>) in the project root directory.</li>
  <li>Open the <code>anomaly_dtection_stgi.ipynb</code> notebook in Jupyter Notebook or JupyterLab.</li>
  <li>Execute the notebook cells to preprocess the data, perform feature engineering, and create the target variable.</li>
  <li>Save the preprocessed data to a file:</li>


<pre><code>data.to_csv("preprocessed_data.csv", index=False)
</code></pre>

 
 
 
 
 
<h3>Model Training</h3>


  <li>Open the <code>anomaly_dtection_stgi.ipynb</code> notebook in Jupyter Notebook or JupyterLab.</li>
  <li>Execute the notebook cells to load the preprocessed data, split it into training and testing sets, and train the model.</li>
  <li>Save the trained model to a file, such as a pickle file (.pkl), for future use and deployment. This file will be used to load the trained model during the anomaly detection process. </li>


<pre><code>import pickle

with open("regressor_model.pkl", 'wb') as file:
    pickle.dump(regressor, file)
</code></pre>
 
 
 
 

<h3>Running the FastAPI Server</h3>

  <li>Open the <code>fast_api.py</code> file.</li>
  <li>Update the file path to the trained model:</li>


<pre><code>with open("regressor_model.pkl", 'rb') as file:
    model = pickle.load(file)
</code></pre>
 
 <li>
        Open the terminal and navigate to the project folder:
        <pre><code>cd anomaly-detection-project</code></pre>
      </li>


  <li>Run the FastAPI server:</li>


<pre><code>uvicorn main:app --reload
</code></pre>


  <li>Open your web browser and visit <a href="http://localhost:8000">http://localhost:8000</a> to ensure the server is running. You should see a "Hello, World!" message.</li>


<h3>Detecting Anomalies</h3>


  <li>To detect anomalies, make a POST request to the <code>/detect</code> endpoint using an API client like cURL or Postman.</li>
  <li>Set the request URL to <code>http://localhost:8000/detect</code> and provide the following JSON payload:</li>


<pre><code>{
    "Country": &lt;country_value&gt;,
    "Device_Type": &lt;device_type_value&gt;,
    "Login_Successful": &lt;login_successful_value&gt;,
    "LoginRatio": &lt;login_ratio_value&gt;,
    "Final_Browser_Category": &lt;final_browser_category_value&gt;,
    "Total_Device_Types": &lt;total_device_types_value&gt;,
    "Total_IP_Addresses": &lt;total_ip_addresses_value&gt;,
    "Total_Countries": &lt;total_countries_value&gt;,
    "Total_Browser_Categories": &lt;total_browser_categories_value&gt;,
    "Time_Difference_in_sec": &lt;time_difference_value&gt;
}
</code></pre>

<ol start="3">
  <li>Replace the <code>&lt;value&gt;</code> placeholders with the corresponding feature values for anomaly detection.</li>
  <li>The API will respond with the predicted anomaly status for the provided data.</li>
</ol>

<h2>Contributing</h2>

<p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>

<h2>License</h2>
<body>
<p>MIT</p>
