import sys

sys.path.append('../../util')
from helper import *
import plot_defaults

parser = argparse.ArgumentParser()
parser.add_argument('--files', '-f',
                    help="Dequeue sample files",
                    required=True,
                    action="store",
                    nargs='+',
                    dest="files")

parser.add_argument('--expected',
                    required=True,
                    action="store",
                    nargs='+',
                    dest="expected")

parser.add_argument('--labels',
                    required=True,
                    action="store",
                    nargs='+',
                    dest="labels")

parser.add_argument('--out', '-o',
                    help="Output png file for the plot.",
                    default=None, # Will show the plot
                    dest="out")

parser.add_argument('--title',
                    default="CDF of percentage of inter-dequeue time\ndeviation from that of an ideal link")

args = parser.parse_args()

def read_samples(f):
    lines = [float(line) for line in open(f).xreadlines()]
    return lines

for f,exp,label in zip(args.files, args.expected, args.labels):
    samples = read_samples(f)
    exp = float(exp)
    normalised = [(sample / exp - 1.0) * 100.0 for sample in samples]

    x, y = cdf(normalised)
    plt.plot(x, y, lw=2, label=label)

plt.legend(loc="lower right")
plt.xlabel("Percentage deviation from expected")
plt.ylabel("Fraction")
plt.title(args.title)
plt.xscale("log")
plt.ylim((0, 1))
plt.grid(True)

if args.out:
    plt.savefig(args.out)
else:
    plt.show()

