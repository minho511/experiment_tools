# experiment_tools



___
- Grad CAM
    
    > [jacobgil/pytorch-grad-cam](https://github.com/jacobgil/pytorch-grad-cam)
    
    1. clone git repo
        ```shell
        git clone https://github.com/jacobgil/pytorch-grad-cam.git
        ```
    2. import 
        ```python
        sys.path.append(os.path.dirname('path of repo'))

        from pytorch_grad_cam import GradCAMPlusPlus
        from pytorch_grad_cam.utils.image import show_cam_on_image
        from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
        ```
    3. Grad CAM visualization
        ```python
        model = # ex. resnet50
        cam = GradCAMPlusPlus(model = model, target_layers = [model.layer4[-1]]) # last conv layer
        outputs = model.forward(inputs)
        target = [ClassifierOutputTarget(label.data)] # 1 sample
        grayscale_cam = cam(input_tensor=inputs, targets=target)
        grayscale_cam = grayscale_cam[0, :]
        rgb_img = # original rgb image
        visualization = show_cam_on_image(rgb_img, grayscale_cam, use_rgb=True, image_weight=0.7)
        plt.imshow(visualization)
        plt.show()
        ```
