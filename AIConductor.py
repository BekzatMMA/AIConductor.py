import time

class AIConductor:
    def __init__(self, orchestra):
        self.orchestra = orchestra

    def conduct(self, duration):
        print("Starting the performance...")
        time.sleep(1)

        for section in self.orchestra:
            print("Conducting", section, "section...")
            time.sleep(2)

        print("Performance complete.")

def main():
    orchestra = ["Strings", "Brass", "Woodwinds", "Percussion"]

    conductor = AIConductor(orchestra)
    conductor.conduct(5)

if __name__ == "__main__":
    main()
