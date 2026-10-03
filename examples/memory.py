from examples.core import PreferenceMemory
if __name__ == '__main__':
    memory = PreferenceMemory()
    memory.put('demo','user1','language','English',ttl=10,now=100)
    print(memory.get('demo','user1','language',now=105))
    print('Other tenant:',memory.get('other','user1','language',now=105))
    print('Expired:',memory.get('demo','user1','language',now=111))
