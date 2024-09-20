import torch


def build_optimizer(args, model):
    classifier_params = []
    backbone_params = []
    for name, p in model.named_parameters():
        if p.requires_grad == False:
            continue
        elif 'classifier' in name:
            classifier_params.append(p)
        else:
            backbone_params.append(p)

    parameters = []
    parameters.append({'params':backbone_params, 'lr':args.lr_backbone, 'weight_decay': args.wd})
    parameters.append({'params':classifier_params, 'lr':args.lr_head, 'weight_decay': args.wd})
    optimizer = torch.optim.AdamW(parameters, betas=(0.9, 0.999))
    print(f"backbone lr : {args.lr_backbone}")
    print(f"classifier lr : {args.lr_head}")
    return optimizer