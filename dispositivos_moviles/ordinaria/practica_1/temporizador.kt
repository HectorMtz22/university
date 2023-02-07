fun main() { 
    var hours: Int
    var min: Int
    var sec: Int
    while (true) {
        try {
            // read the time
            print("Ingresa el tiempo en HH:MM:SS: ")
            val time = readLine()!!.split(":").map { it.toInt() }
            // destructuring time
            hours = time[0]
            min = time[1]
            sec = time[2]
            // validate time
            if (hours < 0 || min < 0 || sec < 0 || time.size != 3 || min > 59 || sec > 59) {
                throw Exception("El valor ingresado no es válido")
            }
            // sounds good 
            break
        }
        catch(e: Exception) {
            println("El valor ingresado no es válido")
        }
    }
    

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
