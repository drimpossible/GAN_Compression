import argparse

dset_choices = ['cifar10','cifar100','imagenet12']
reporttype_choices = ['acc']
criterion_choices = ['crossentropy']
optim_choices = ['sgd','adam']
model_def_choices = ['vgg16_bn']

def myargparser():
    parser = argparse.ArgumentParser(description='GAN Compression...')

    #data stuff
    parser.add_argument('--dataset', choices=dset_choices, help='chosen dataset'+'Options:'+str(dset_choices))
    parser.add_argument('--data_dir', required=True, help='Dataset directory')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--workers', default=4, type=int, help='number of data loading workers (Default: 4)')
    parser.add_argument('--weight_init', action='store_true', help='Turns on weight inits')
    #other default stuff
    parser.add_argument('--epochs', required=True, type=int,help='number of total epochs to run')
    parser.add_argument('--batch-size', required=True, type=int, help='mini-batch size (default: 128)')
    parser.add_argument('--nclasses', help='number of classes', default=0)
    parser.add_argument('--printfreq', default=50, type=int, help='print frequency (default: 10)')
    parser.add_argument('--learningratescheduler', required=True, help='print frequency (default: 10)')
    parser.add_argument('--revLabelFreq', required=True, type=int, help='print frequency (default: 10)')

    #optimizer/criterion stuff
    parser.add_argument('--decayinterval', type=int, help='decays by a power of decay_var in these epochs')
    parser.add_argument('--decaylevel', type=float, help='decays by a power of decaylevel')
    parser.add_argument('--optimType', required=True, choices=optim_choices, type=str, help='Optimizers. Options:'+str(optim_choices))

    parser.add_argument('--maxlr', required=True, type=float, help='initial learning rate')
    parser.add_argument('--lr', type=float, help='initial learning rate')
    parser.add_argument('--minlr', required=True, type=float, help='initial learning rate')

    parser.add_argument('--nesterov', action='store_true', help='nesterov momentum')
    parser.add_argument('--momentum', default=0.9, type=float, help='momentum (Default: 0.9)')
    parser.add_argument('--weightDecay', default=0, type=float, help='weight decay (Default: 1e-4)')

    #extra model stuff
    parser.add_argument('--name', required=True, type=str, help='name of experiment')
    parser.add_argument('--teacher_filedir', required=True, type=str, help='name of experiment')
    parser.add_argument('--student_filedir', type=str, help='name of experiment')

    #default
    parser.add_argument('--cachemode', default=True, help='if cachemode')
    parser.add_argument('--cuda', default=True, help='If cuda is available')
    parser.add_argument('--manualSeed', type=int, default=123, help='fixed seed for experiments')
    parser.add_argument('--ngpus', type=int, default=1, help='no. of gpus')
    parser.add_argument('--logdir', type=str, default='../logs', help='log directory')
    parser.add_argument('--tensorboard',help='Log progress to TensorBoard', default=True)
    parser.add_argument('--testOnly',  default=False, help='run on validation set only')
    parser.add_argument('--acc_type', default = "class")

    parser.add_argument('--start-epoch', default=0, type=int, help='manual epoch number (useful on restarts)')
    parser.add_argument('--pretrained', action='store_true', help='use pre-trained model')
    parser.add_argument('--pretrained_file', default='')

    #Hyperparameters
    parser.add_argument('--wdiscAdv', default=0.3, type=float, help='Weight of discrim adv loss')
    parser.add_argument('--wdiscClassify', default=0.4, type=float, help='Weight of discrim classification loss')
    parser.add_argument('--wstudSim', default=0.5, type=float,  help='Weight student reconstruction')
    parser.add_argument('--wstudDeriv', default=600, type=float,  help='Weight student derivative')

    parser.add_argument('--label_reversal_freq', dest='augment', action='store_false', help='whether to use standard augmentation (default: True)')

    parser.add_argument('--from_modelzoo', action='store_true')
    #model stuff
    parser.add_argument('--resume', default='', type=str, metavar='PATH',
                        help='path to latest checkpoint (default: none)')
    parser.add_argument('--store', default='', type=str, metavar='PATH',
                        help='path to storing checkpoints (default: none)')
    parser.add_argument('--evaluate', dest='evaluate', action='store_true',
                        help='evaluate model on validation set')


    return parser
