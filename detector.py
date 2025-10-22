from ultralytics import YOLO
import cv2

class Detector:
    def __init__(self, model_name='yolov8n.pt'):
        self.model = YOLO(model_name)
        self.class_names = self.model.names

    def detect(self, frame, target_class=None):
        results = self.model(frame, verbose=False)[0]
        detections = []
        count = 0
        for box in results.boxes:
            cls_id = int(box.cls[0])
            cls_name = self.class_names[cls_id]
            if (target_class is None) or (cls_name == target_class):
                count += 1
                xyxy = box.xyxy[0].cpu().numpy().astype(int)
                detections.append({
                    'bbox': xyxy,
                    'class': cls_name,
                    'conf': float(box.conf[0])
                })
        return detections, count

    def get_available_classes(self):
        return list(self.class_names.values()) 