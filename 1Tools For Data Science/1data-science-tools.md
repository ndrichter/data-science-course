# Data Science Tools
## Categories of Data Science Tools
- Data management: process of persisting and retrieving data
- Data integration and transformation (ETL): process of retrieving data from remote data management systems
- Data visualization: visually exploring the data, often a final deliverable
- Model Building: process of creating a machine learning or deep learning model using an appropriate algorithm
- Model deployment: ML or DL model available to third party applications
- Model Monitoring and Assessment: ensure quality/accurate performance
- Code asset management: versioning and other collaborative features to facilitate teamwork
- Data asset management: supports replication, back, and access right management
- Development environments (IDEs): tools that help the data scientist to implement, execute, test and deploy their work
- Execution environments: tools where data processing, model training, and deployment take place
- Fully integrated visual tools: incorporates all the categories above

## Open Source Tools for Data Science - Part 1
- Mostly widely used data management tools are for relational databases: MySQL, PostgreSQL
    - For NoSQL: CouchDB, Cassandra
    - For file based: Hadoop, Ceph
    - Index-able search on text for document retrieval: Elasticsearch
    
- ETL: extract, transform, and load (data refining and cleaning )
    - Apache Airflow
    - Kubeflow (used on top of Kubernetes)
    - Apache Kafka
    - Apache Nifi (nice visual editor)
    - Spark SQL
    - Node-RED, can run on raspberry pi
    
- Data visualization tools
    - Hue: create visualizations from SQL queries
    - Kibana, limited to the data provider Elasticsearch
    - Superset web application
    
- Model Deployment, important to make it available to others
    - PredictionIO, only supports Apache Spark models
    - Seldon supports nearly every framework
    - Mleap
    - TensorFlow Service/Lite/JS
    
- Model Monitoring, need to keep track of its performance
    - ModelDB to manage ML models
    - Prometheus
    - IBM AI Fairness 360 Open Source Toolkit, evaluates bias in models (like gender and race)
    - IBM Adversarial Robustness 360 Toolbox, evaluate against manipulative data that harms the model
    - IBM AI Explainability 360, makes ML models more understandable 
    
- Code asset management
    - Git is the standard
    - GitHub and GitLab
    - Bitbucket
    
- Data Asset Management, manage versions and metadata
    - Apache Atlas
    - ODPi Egeria
    - Kylo
    
## Open Source Tools for Data Science - Part 2
- Development environments
    - Jupyter, kernals allow for different languages. Allows for cohesive documentation, code and visualization. Jupyter Lab next iteration
    - Apache Zeppelin. Plotting capability without coding.
    - R Studio, unifies programming, execution, debugging, remote data access, data exploration and visualization
    - Spyder, alternative to R Studio
    
- Execution Environments
    - Apache Spark, linear scalability. Batch data processing engine
    - Apache Flink. More focused on processing real time data streams
    - RiseLab Ray. Large scale model training
    
- Fully integrated Visual Tools (Programming not necessary)
    - Knime. Drag and drop capabilities with visualization
    - Orange. Less flexible but easier to use
    
## Commercial Tools for Data Science
- Data management: Oracle, Microsoft SQLServer, IBM DB2
- ETL: Informatica, IBM InfoSphere DataStage, Talend, IBM Watson Studio Desktop
- Data visualization: Tableau, Microsoft Power BI, IBM Cognos Analytics
- Model Building: SPSS, SAS
- Model deployment: SPSS software suite/services
- Model monitoring: nothing relevant yet, open source first choice
- Data asset management: Informatica, IBM InfoSphere Information Governance Catalog
- Watson Studio Desktop IDE for data scientist
- H20.ai - fully integrated visual tool

## Cloud based Tools for Data Science
- Fully integrated visual tools and platforms
    - Watson Studio with Watson OpenScale
    - Microsoft Azure Machine Learning
    - H20.ai
    
- Data management (SAAS offerings)
    - Amazon DynamoDB
    - Cloudant (under the hood CouchDB)
    - IBM DB2
    
- ETL or ELT
    - Informatica
    - IBM Data Refinery
    
- Data Visualization
    - Datameer
    - IBM Cognos Analytics
    - IBM Data Refinery
    
- Model building
    - IBM Watson Machine Learning
    - Google Cloud
    
- Model Deployment
    - Usually tightly integrated with model building process (SPSS)
    
- Model Monitoring
    - Amazon SageMaker Model Monitor
    - Watson OpenScale
    
## 















