from metaflow import FlowSpec, step, batch


class CheckIp(FlowSpec):
    @step
    def start(self):
        import urllib.request
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        print("IP:", external_ip)
        self.next(self.check)
 
    @batch
    @step
    def check(self):
        import urllib.request
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        print("IP in compute environment:", external_ip)
        self.next(self.end)
 
    @step
    def end(self):
        print("End")
 
 
if __name__ == "__main__":
    CheckIp()
