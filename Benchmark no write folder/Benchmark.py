from time import perf_counter
import os
import subprocess

#To_benchmark = ["nbody.py", "nbody_release.exe", "nbody_debug.exe"]
To_benchmark = ["nbody.py", "nbody_release_nowrite.exe", "nbody_debug_nowrite.exe"]
Simul_sizes = [5000, 500000, 5000000, 50000000]

def write_runtimes(p_list, size_list):
    """Calls count runtime for all programmes in p_list & over and all simulation sizes in size_list and
    writes these to a file

    :param p_list: A list with all executables to be called
    :param size_list: A list with all simulation sizes to run
    :return: None
    """
    with open("Benchmark runs.txt", "w") as fh:
        for programme in p_list:
            for simsize in size_list:
                fh.write("The programme {} with n-size {}, has a runtime of {} seconds \n".
                         format(programme, simsize,  count_runtime(programme, simsize)))


def count_runtime(name, n_size = 1):
    """
    Returns the runtime of executable 'name' in seconds

    :param name: The name of the executable
    :type name: string
    :param n_size: The size to be fed to the executable for the simulation
    :type n_size: Integer
    :return: The runtime in seconds
    """

    name.strip()        #should we want to generalize to user-input given filenames
    if name[-1] == "y":
        command = "py " + name + " " + str(n_size)
    else:
        command = name + " " + str(n_size)

    start = perf_counter()
    subprocess.call(command)
    stop = perf_counter()

    return stop-start

if __name__ == "__main__":
    write_runtimes(To_benchmark, Simul_sizes)
