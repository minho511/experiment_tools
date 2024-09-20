## SAM Optimizer
link : https://github.com/davda54/sam
___

- import
    ```python
    from sam import SAM
    ```

- build optimizer
    ```python
    optimizer = SAM(model.parameters(), nn.ADAM, 
                    lr=args.lr, weight_decay=0.01, nesterov=True)
    ```
- train loop
    ```python
    for epoch in range(EPOCH):
        for i, sample in enumerate(tqdm(train_dataloader)):
            optimizer.zero_grad()
            out = net(sample)
            loss = criterion(out, labels)
            loss.backward()
            optimizer.first_step(zero_grad=True)
            
            loss = criterion(net(sample), labels).backward()
            optimizer.second_step(zero_grad=True)
    ```