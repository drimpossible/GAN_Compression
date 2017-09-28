bash clean.sh;CUDA_VISIBLE_DEVICES=0 python3 main.py --data_dir '../data' --epochs 90 --batch-size 128 --optimType sgd --maxlr 0.1 --minlr 0.0005 --name 'test' --teacher_filedir '../checkpoint/teachervgg_94.05.tar' --student_filedir '../checkpoint/cifar_quick_cifar10_best.pth.tar' --dataset 'cifar10' --learningratescheduler='none' --revLabelFreq 20 --verbose
