import speedtest

test = speedtest.Speedtest()
# Get all servers
print("Server List Loading")
test.get_servers()
# Choose best server
print("Choosing Best Server")
best_serv = test.get_best_server()
# print best server details
print(
    f"Details found [Hostname: {best_serv['host']},Located in {best_serv['country']} {best_serv['name']},Sponsored by {best_serv['sponsor']}]"
)
# Perform download test
print("Performing Download Test...")
Download_test = test.download()
# Perform upload test
print("Performing Upload Test...")
Upload_test = test.upload()
# Perform ping test
print("Performing Ping Test...")
ping = test.results.ping

# print result
print(f"Download result: {Download_test /1024 / 1024:.2f} Mb/s")
print(f"Upload result: {Upload_test /1024 /1024:.2f} Mb/s")
print(f"ping: {ping:.2f} ms")

# print("\n", "All Server Info Below", "\n", best_serv, "\n")
