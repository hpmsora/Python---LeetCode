"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def __init__(self):
        self.internalBuffer = [''] * 4
        self.internalBufferSize = 0
        self.internalBufferPointer = 0

    def read(self, buf, n):
        totalCharsRead = 0

        while totalCharsRead < n:
            # If the internal buffer is empty, read from the file
            if self.internalBufferPointer == self.internalBufferSize:
                self.internalBufferSize = read4(self.internalBuffer)
                self.internalBufferPointer = 0

            # If no more characters are left in the file, break
            if self.internalBufferSize == 0:
                break

            # Copy from internal buffer to the destination buffer
            while totalCharsRead < n and self.internalBufferPointer < self.internalBufferSize:
                buf[totalCharsRead] = self.internalBuffer[self.internalBufferPointer]
                totalCharsRead += 1
                self.internalBufferPointer += 1

        return totalCharsRead
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        