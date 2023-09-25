import psutil


def get_cpu_info():
    data = psutil.cpu_times()
    info = {"uses": data.uses}

    return info


def get_mem_info():
    info = {}
    ...
    return info


def cpu_show(cpu_i):
    tmpl = "{}"
    print(tmpl.format(**cpu_i))


def show(cpu, mem, proc):
    ...
    cpu_show(cpu)


def main():
    cpu_info = get_cpu_info()
    memory_info = get_mem_info()


if __name__ == '__main__':
    main()
