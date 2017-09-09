import argparse
from ui import UI

# TODO
#
# Coloured paths if there are hexagons of multiple colours and symmetry
#  - each path must go through its own colour of hexagons
#  - either path can go through black hexagons
#
# Capture puzzles from the screen (using PIL?) and automatically load and solve
# them
#
# Store known puzzles, names for puzzles and found solutions in a database
# Present these as a list from which puzzles can be selected


# Optimisations
#
# These should be proven with benchmarks
#
# When an area has been checked, store the path defining that area in a tree
# (possibly a dictionary of dictionaries) where each node in the tree is a node
# in the path.  The final node should be true (this path leads to a valid area)
# or false.  Then, when a path is being drawn, this tree (maybe called
# area_validation) can be checked a node at a time and, if an invalid area is
# created, we know this path is invalid and no other paths should be pushed onto
# the queue.  Also store the reverse path in the area_validation tree as an area
# can be defined both ways.
#  - the whole path which defines the area must be stored (including paths
#    around the edge of the puzzle) because these may affect the validity of the
#    area
#
# If there are no elimination marks on the board at all, solve triangles and
# hexagons for the whole board at once, rather than defining areas

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="""\
TTWS - The \"The Witness\" Solver""")
  parser.add_argument("-p", "--puzzle",
                      help="A single puzzle code (puzzle state encoded from "
                           "https://windmill.thefifthmatt.com)")
  parser.add_argument("-f", "--file",
                      help="File containing a list of puzzle codes")

  args = parser.parse_args()

  puzzles = []
  if args.puzzle:
    puzzles = [args.puzzle]
  elif args.file:
    puzzles = [line.strip() for line in open(args.file).readlines()]

  # Preload the UI with none, one or many puzzle codes
  UI(puzzles)
