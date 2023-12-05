import networkx as nx
import matplotlib.pyplot as plt

def creategraph(teachers, subjects, classes, n, m):
    G = nx.MultiGraph()

    # Create a list of colors for each edge
    edge_colors = []

    timetable = []

    for i in range(n):
        for j in range(m):
            if classes[i][j] != 0:
                for k in range(classes[i][j]):
                    str1 = "T" + str(i + 1)
                    str2 = "S" + str(j + 1)
                    ed = (str1, str2)

                    # Add a different color for each edge
                    edge_colors.append(f"C{k + 1}")

                    # Add an edge only if it doesn't exist already
                    if not G.has_edge(str1, str2):
                        G.add_edge(str1, str2)
                        timetable.append(f"Period {k + 1}: {str1} - {str2}")

    pos = nx.circular_layout(G)

    # Draw edges with different colors
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=800, font_size=10,
            edge_color=edge_colors, arrowsize=20)

    plt.title("Time Table")
    plt.show()

    # Print the timetable

def create_timetable_matrix(teachers, subjects, classes, n, m):
    timetable_matrix = [["" for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if classes[i][j] != 0:
                for k in range(classes[i][j]):
                    str1 = "T" + str(i + 1)
                    str2 = "S" + str(j + 1)
                    period = k + 1

                    # Assign the period to the matrix
                    timetable_matrix[i][j] = f"{str1}-{str2}"

    return timetable_matrix

def print_timetable_matrix(matrix, teachers, subjects):
    print("\nTime Table:")
    print("\t", end="")
    for subject in subjects:
        print(subject, end="\t")
    print()
    for i, row in enumerate(matrix):
        print(teachers[i], end="\t")
        for entry in row:
            print(entry, end="\t")
        print()

if __name__ == "__main__":
    n = int(input("Enter number of teachers: "))
    teachers = [f"T{i}" for i in range(1, n + 1)]

    m = int(input("Enter number of subjects: "))
    subjects = [f"S{i}" for i in range(1, m + 1)]

    classes = []

    print("\nEnter number of periods required:")
    for i in range(n):
        print("Enter for teacher", (i + 1), ":")
        cls = []
        for j in range(m):
            print("Enter for subject", (j + 1), ":")
            k = int(input())
            cls.append(k)
        classes.append(cls)

    print("\nTeachers:", teachers)
    print("Subjects:", subjects)
    print("Classes:", classes)

    # Graph Visualization
    creategraph(teachers, subjects, classes, n, m)

    # Timetable Matrix
    timetable_matrix = create_timetable_matrix(teachers, subjects, classes, n, m)
    print_timetable_matrix(timetable_matrix, teachers, subjects)