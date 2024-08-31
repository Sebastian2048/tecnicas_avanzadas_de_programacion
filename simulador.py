from Simpy import *

def machine(env, name, failure_rate):
    while True:
        yield env.timeout(failure_rate)
        print(f'{name} ha fallado en el tiempo {env.now}')

def main():
    env = simpy.Environment()
    env.process(machine(env, 'Máquina 1', 5))
    env.process(machine(env, 'Máquina 2', 7))
    env.run(until=20)

if __name__ == '__main__':
    main()
