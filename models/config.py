import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='deblur arguments')
    parser.add_argument('--phase', type=str, default='test', help='determine whether train or test')
    parser.add_argument('--datalist', type=str, default='..\\datalist_gopro.txt', help='training datalist')
    parser.add_argument('--model', type=str, default='color', help='model type: [lstm | gray | color]')
    parser.add_argument('--batch_size', help='training batch size', type=int, default=16)
    parser.add_argument('--epoch', help='training epoch number', type=int, default=4000)
    parser.add_argument('--lr', type=float, default=1e-4, dest='learning_rate', help='initial learning rate')
    parser.add_argument('--gpu', dest='gpu_id', type=str, default='0', help='use gpu or cpu')
    parser.add_argument('--net', type=str, default='DMPHN')
    parser.add_argument('--height', type=int, default=720,
                        help='height for the tensorflow placeholder, should be multiples of 16')
    parser.add_argument('--width', type=int, default=1280,
                        help='width for the tensorflow placeholder, should be multiple of 16 for 3 scales')
    parser.add_argument('--n_feat', type=int, default=32)
    parser.add_argument('--kernel_size', type=int, default=3)
    parser.add_argument('--num_resb', type=int, default=3)
    parser.add_argument('--input_path', type=str, default='./testing_set',
                        help='input path for testing images')
    parser.add_argument('--output_path', type=str, default='./testing_res',
                        help='output path for testing images')
    args = parser.parse_args()
    return args