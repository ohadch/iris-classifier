### Train
`python3 retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps 500 --model_dir=inception --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --image_dir flower_photos/`

### Predict
`python3 label_image.py — graph=retrained_graph.pb — image=test_images/rose.jpg — labels=retrained_labels.txt — output_layer=final_result — input_layer=Placeholder`