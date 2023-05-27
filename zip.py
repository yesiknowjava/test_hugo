import multiprocessing
import time
import datetime
from pathlib import Path

def create_service_md(zip_chunk_list):
    curr_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%S")
    for zip_code in zip_chunk_list:
        data_folder = Path("content/ziptest/")
        file_name = str(zip_code) + ".md"
        filepath = data_folder / file_name
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

    def generate_zip_list(self):
        data_folder = Path("zip.csv")
        with open(data_folder, 'r') as w:
            self.zip_list = w.readline().split(",")
    
    def __init__(self) -> None:
        self.slice_count = 25
        self.zip_list = [] 
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
    from pathlib import Path
    obj = ZipSplit()
    obj.generate_zip_list()
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
    t1 = time.time()
    main()
    t2 = time.time()
    print(t2-t1)