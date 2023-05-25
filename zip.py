import multiprocessing
import time
import datetime

def create_service_md(zip_chunk_list):
    curr_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%S")
    for zip_code in zip_chunk_list:
        print("in thread")
        filepath = "/content/ziptest/"+str(zip_code)+".md"
        filepath = "C:\\Users\\linuxfullstackdev\\Documents\\projects\\technetguide\\content\\ziptest\\"+str(zip_code)+".md"
        fileobj = open(filepath,"w+")
        l1 = "+++\n"
        l2 = 'title= "Good Title\n"'
        l3 = "date= "+curr_date+"\n"
        l4 = "draft= false"+"\n"
        l5 = 'category= "test"\n'
                        
                            
        l7 = "+++"+"\n"
        content_file = 'Simple example {{.Params.Keyword}} significantly'
        data = l1+l2+l3+l4+l5+l7+content_file
        fileobj.write(data)
        fileobj.close()
    print("thread completed")

class ZipSplit():
    
    __slots__ = ('slice_count', 'zip_list', 'errors')
    
    def __init__(self) -> None:
        self.slice_count = 25
        self.zip_list = [i for i in range(1, 500)]
        self.errors = []

    def has_errors(self):
        if len(self.errors) > 0:
            return True
    
    def split_zip_chunks(self):
        for i in range(0, len(self.zip_list), self.slice_count):
            yield self.zip_list[i:i + self.slice_count]
    
    def yield_zip_chunk(self, zip_chunk):
        return zip_chunk
    
def main():
    print("Hello World!")
    
    # from pathlib import Path
    # Path("/content/ziptest").mkdir(parents=True, exist_ok=True)

    from pathlib import Path
    Path("C:\\Users\\linuxfullstackdev\\Documents\\projects\\technetguide\\content\\ziptest").mkdir(parents=True, exist_ok=True)
    obj = ZipSplit()
    gen_obj = obj.split_zip_chunks()
    processes = []
    for zip_chunk in gen_obj:
        zip_chunk_list = obj.yield_zip_chunk(zip_chunk)
        print(zip_chunk_list, len(zip_chunk_list))
        p = multiprocessing.Process(target=create_service_md, args=(zip_chunk_list,))
        p.start()
        processes.append(p)

    # Joins all the processes
    for p in processes:
        p.join()
    print("Process Completed successfully")

if __name__ == "__main__":
    main()