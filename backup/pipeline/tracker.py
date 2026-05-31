import math


class CentroidTracker:

    def __init__(self):

        self.next_id = 1

        self.objects = {}

    def update(self, detections):

        updated_objects = {}

        for detection in detections:

            x1, y1, x2, y2 = detection

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            matched_id = None

            min_distance = 999999

            for obj_id, center in self.objects.items():

                distance = math.sqrt(
                    (cx - center[0]) ** 2
                    + (cy - center[1]) ** 2
                )

                if distance < 200:

                    if distance < min_distance:

                        min_distance = distance

                        matched_id = obj_id

            if matched_id is None:

                matched_id = self.next_id

                self.next_id += 1

            updated_objects[matched_id] = (cx, cy)

        self.objects = updated_objects

        return self.objects