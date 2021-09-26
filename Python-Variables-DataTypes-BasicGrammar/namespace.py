

# ----- Namespace -----


# Build-in Namespace
# Module: Global Namespace
# Function:Local Namespace


def outer():
    outer_number = 100

    def inner():
        inner_number = 200
        print("Inner number =", inner_number)

    inner()


global_number = 300


outer()
