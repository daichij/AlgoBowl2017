
def firstPass( tasks, machSpeeds ):
    avgWeight = sum( tasks ) / sum( machSpeeds )

    idealMachWeights = [w * avgWeight for w in machSpeeds]

    machines = [{'max_runtime' : w, 'speed' : machSpeeds[i], 'tasks' : [], 'runtime' : 0} for i,w in enumerate(idealMachWeights)]

    for i in reversed(range(len(machSpeeds))):
        if i == 0:
            machines[i]['tasks'] = tasks
            machines[i]['runtime'] = sum(tasks)
        else:
            while machines[i]['runtime'] < machines[i]['max_runtime']:
                if not tasks:
                    return machines

                t_task = tasks.pop()
                machines[i]['tasks'].append(t_task)
                machines[i]['runtime'] += t_task
   

    return machines