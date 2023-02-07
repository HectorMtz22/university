fun main() { 
    print("Ingresa el tiempo en HH:MM:SS: ")
    // read the time
    val time = readLine()!!.split(":").map { it.toInt() }
    // destructuring time
    var hours = time[0]
    var min = time[1]
    var sec = time[2]

    while (hours >= 0) {
        while (min >= 0) {
            while (sec >= 0) {
                // print time with 0s
                println("%02d:%02d:%02d".format(hours, min, sec))
                Thread.sleep(1000L)
                sec--
            }
            sec = 59
            min--
        }
        min = 59
        hours--
    }
    println("Llegaste a la meta!")
} 
