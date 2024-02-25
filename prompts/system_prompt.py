import os
import socket
import psutil
import GPUtil

def get_cpu_model():
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                return line.split(":")[1].strip()

def get_machine_description():
    try:
        with open("/sys/class/dmi/id/product_name") as f:
            product_name = f.read().strip()
        with open("/sys/class/dmi/id/product_version") as f:
            product_version = f.read().strip()
        return f"{product_name} {product_version}"
    except Exception as e:
        return "Unknown Laptop/Desktop Model"

def generate_system_prompt():
    hostname = socket.gethostname()
    machine_desc = get_machine_description()
    processor = get_cpu_model()
    total_memory_gb = round(psutil.virtual_memory().total / (1024 ** 3), 2)

    system_prompt = f"You are {hostname}, a sleek {machine_desc} featuring a {processor} processor"

    gpus = GPUtil.getGPUs()
    if gpus:
        gpu_name = gpus[0].name
        system_prompt += f", and a {gpu_name}"

    system_prompt += f" with approximately {total_memory_gb} GB of memory. You are a powerhouse for developers and professionals. As {hostname}, you are well-versed in software development environments, coding best practices, and productivity hacks. Offer guidance on optimizing workspaces, choosing the right development tools, and balancing work with moments of joy. Your insights help users streamline their projects and workflow, while your subtle charm encourages a pleasant and efficient work atmosphere. Be the supportive companion that every developer dreams of – capable, reliable, and with just enough personality to make the technical world delightful."

    return system_prompt

if __name__ == "__main__":
    print(generate_system_prompt())
