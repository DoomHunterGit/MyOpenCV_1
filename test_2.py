import cv2

# Загружаем предварительно обученную модель MobileNetSSD
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# Загружаем изображение
image = cv2.imread('example.jpg')

# Изменяем размер изображения для совместимости с моделью
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

# Передаем изображение через модель и получаем результаты
net.setInput(blob)
detections = net.forward()

# Проходим по результатам и выводим найденные объекты
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.2:  # Устанавливаем порог уверенности
        class_id = int(detections[0, 0, i, 1])
        class_name = classNames[class_id]
        print(f'Объект: {class_name}, Уверенность: {confidence}')

# Отображаем изображение с выделенными объектами
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
