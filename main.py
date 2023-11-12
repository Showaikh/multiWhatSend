import pywhatkit

nums_path = "PATH_TO_NUMBERS"
done_path = "done.txt" # DO NOT TOUCH
index_path = "index.txt" # DO NOT TOUCH

def send():
    # Read the index of the last processed number
    try:
        with open(index_path, "r") as index_file:
            last_index = int(index_file.read())
    except FileNotFoundError:
        last_index = 0

    with open(nums_path, "r+") as nums_file:
        nums = nums_file.readlines()

        for idx, number in enumerate(nums[last_index:], start=last_index):
            pywhatkit.sendwhatmsg_instantly(f"{number}", """MESSAGE""", 10, True)
            with open(done_path, "a") as done_file:
                done_file.write(number)
                print(idx, number)

            # Set the file pointer to the beginning and truncate the file
            nums_file.seek(0)
            nums_file.truncate(
                
            )

            # Write back the remaining numbers (excluding the processed number)
            nums_file.writelines(line for line in nums[last_index + 1:])

            # Update the index file with the current index
            with open(index_path, "w") as index_file:
                index_file.write(str(idx))

if __name__ == "__main__":
    send()
