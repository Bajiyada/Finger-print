class Fingerprint:
    def __init__(self):
        self.image = None
        self.features = None

    def capture_fingerprint(self, camera_index=0):
        import cv2
        cap = cv2.VideoCapture(camera_index)
        ret, self.image = cap.read()
        cap.release()
        if not ret:
            raise Exception("Could not capture fingerprint image.")

    def process_image(self):
        from preprocess import enhance_image, binarize_image
        if self.image is None:
            raise Exception("No image captured to process.")
        enhanced_image = enhance_image(self.image)
        self.image = binarize_image(enhanced_image)

    def extract_features(self):
        if self.image is None:
            raise Exception("No image available for feature extraction.")
        # Placeholder for feature extraction logic
        self.features = "Extracted features from the fingerprint image."  # Replace with actual feature extraction logic
        return self.features        from flask import Flask, Response, jsonify
        import cv2
        from fingerprint import Fingerprint
        
        app = Flask(__name__)
        fp = Fingerprint()
        
        @app.route("/capture")
        def capture():
            try:
                fp.capture_fingerprint(camera_index=0)
                if fp.image is None:
                    return jsonify({"error": "no image captured"}), 500
                ret, jpg = cv2.imencode(".jpg", fp.image)
                if not ret:
                    return jsonify({"error": "encoding failed"}), 500
                return Response(jpg.tobytes(), mimetype="image/jpeg")
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        if __name__ == "__main__":
            app.run(host="127.0.0.1", port=5000, debug=True)            // ...existing code...
            from flask import Flask, Response, jsonify
            import cv2
            from fingerprint import Fingerprint
            
            app = Flask(__name__)
            fp = Fingerprint()
            
            @app.route("/capture")
            def capture():
                try:
                    fp.capture_fingerprint(camera_index=0)
                    if fp.image is None:
                        return jsonify({"error": "no image captured"}), 500
                    ret, jpg = cv2.imencode(".jpg", fp.image)
                    if not ret:
                        return jsonify({"error": "encoding failed"}), 500
                    return Response(jpg.tobytes(), mimetype="image/jpeg")
                except Exception as e:
                    return jsonify({"error": str(e)}), 500
            
            if __name__ == "__main__":
                app.run(host="127.0.0.1", port=5000, debug=True)
            // ...existing code...            // ...existing code...
            class Fingerprint:
                def __init__(self):
                    self.image = None
                    self.features = None
            
                def capture_fingerprint(self, camera_index=0):
                    import cv2
                    cap = cv2.VideoCapture(camera_index)
                    if not cap.isOpened():
                        cap.release()
                        raise Exception("Could not open camera.")
                    ret, self.image = cap.read()
                    cap.release()
                    if not ret or self.image is None:
                        raise Exception("Could not capture fingerprint image.")
            
                def process_image(self):
                    from preprocess import enhance_image, binarize_image
                    if self.image is None:
                        raise Exception("No image captured to process.")
                    enhanced_image = enhance_image(self.image)
                    self.image = binarize_image(enhanced_image)
            
                def extract_features(self):
                    if self.image is None:
                        raise Exception("No image available for feature extraction.")
                    # Placeholder for feature extraction logic
                    self.features = "Extracted features from the fingerprint image."
                    return self.features
            // ...existing code...y