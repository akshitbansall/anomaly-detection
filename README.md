<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Anomaly Detection Project</h1>
  
  <h2>Anomalous Score >= 3</h2>
   <p>(The result of the mmodel gives the Range from 1-10, so the if the scores is >=3, its a anomalous record)</p>
   
    
  <h2>Table of Contents</h2>
  <ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#algorithms">Algorithms Used</a></li>
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
    <li>Download the dataset:</li>
  </ol>
  <p>
    The dataset used for training and testing the anomaly detection model should be placed in the <code>data</code> directory.
    Make sure to follow the appropriate data format and column structure.
  </p>
  <h2 id="usage">Usage</h2>
  <h3>Data Preparation</h3>
  <ol>
    <li>Place your login data file (<code>Login_Data.csv</code>) in the project root directory.</li>
    <li>Open the <code>anomaly_detection_stgi.ipynb</code> notebook in Jupyter Notebook or JupyterLab.</li>
    <li>Execute the notebook cells to preprocess the data, perform feature engineering, and create the target variable.</li>
    <li>Save the preprocessed data to a file:</li>
  </ol>
  <pre><code>data.to_csv("preprocessed_data.csv", index=False)
</code></pre>
  <h3>Model Training</h3>
  <ol>
    <li>Open the <code>anomaly_detection_stgi.ipynb</code> notebook in Jupyter Notebook or JupyterLab.</li>
    <li>Execute the notebook cells to load the preprocessed data, split it into training and testing sets, and train the model.</li>
    <li>Save the trained model to a file, such as a pickle file (.pkl), for future use and deployment. This file will be used to load the trained model during the anomaly detection process.</li>
  </ol>
  <pre><code>import pickle
 
with open("regressor_model.pkl", 'wb') as file:
    pickle.dump(regressor, file)
</code></pre>
  <h3>Running the FastAPI Server</h3>
  <ol>
    <li>Open the <code>fast_api.py</code> file.</li>
    <li>Update the file path to the trained model:</li>
  </ol>
  <pre><code>with open("regressor_model.pkl", 'rb') as file:
    model = pickle.load(file)
</code></pre>
  <ol start="3">
    <li>Open the terminal and navigate to the project folder:</li>
  </ol>
  <pre><code>cd anomaly-detection-project</code></pre>
  <ol start="4">
    <li>Run the FastAPI server:</li>
  </ol>
  <pre><code>uvicorn fast_api:app --reload
</code></pre>
  <ol start="5">
    <li>Open your web browser and visit <a href="http://localhost:8000">http://localhost:8000</a> to ensure the server is running. You should see a "Hello, World!" message.</li>
  </ol>
  <h3>Detecting Anomalies</h3>
  <ol>
    <li>To detect anomalies, make a POST request to the <code>/docs</code> endpoint using an API client like cURL or Postman.</li>
    <li>Set the request URL to <code>http://localhost:8000/docs</code> and provide the following JSON payload:</li>
  </ol>
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
    <li>The API will respond with the predicted anomaly score for the provided data.</li>
     <li> <h2>(The result of the mmodel gives the Range from 1-10, so the if the scores is >=3, its a anomalous record) Anomalous Score >= 3 </h2></li>
  </ol>
  <h2 id="algorithms">Algorithms Used</h2>
  <p>The following algorithms are used in this project:</p>
  <ul>
    <li>XGBoost: XGBoost is an optimized gradient boosting algorithm that is commonly used for classification and regression tasks. It is known for its speed and performance in handling large datasets.</li>
  </ul>
  
</body>
</html>
