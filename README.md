# iNeuron-e2eObjectDetection1
This is an end to end object detection project form iNeuron by Bappy

# Links
* [github](https://github.com/entbappy/End-to-end-Object-Detection-Project)

# Workflow
* utils
* constants
  * constant/training_pipeline/__init__.py
* config_entity
  * config_entity.py
* artifact_entity
  * artifacts_entity.py
* components
  * data_ingestion.py
  * data_validation.py
* Pipeline
  * Data Ingestion
    * training_pipeline.py
  * Data Validation
    * training_pipeline.py
  * Model Trainer
  * Model Pusher
* main app.py

# Mini Workflow
* constant/training_pipeline/__init__.py
* config_entity.py
* artifacts_entity.py
* components/
  * data_ingestion.py
  * data_validation.py
  * model_trainer.py
* Clone the yolov5 repo and change the 'nc' value to the classes we have in our data yolov5s.yaml
  * the nc value is in the yolo 
* training_pipeline.py
