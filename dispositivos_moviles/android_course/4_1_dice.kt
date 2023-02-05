fun main() {
    val myFirstDice = Dice()
    println("Your ${myFirstDice.numSides} sided dice rolled ${myFirstDice.roll()}!")
    
    val mySecondDice = Dice(20)
    println("Your ${mySecondDice.numSides} sided dice rolled ${mySecondDice.roll()}!")

    val myCoin = Coin()
    println("Your coin flipped ${myCoin.flip()}!")
    
}

class Dice(val numSides: Int = 6) {
    fun roll(): Int {
        return (1..numSides).random()
    }
}

class Coin() {
    fun flip(): String {
        if ((1..2).random() == 1) {
            return "Cara"
        } else {
            return "Cruz"
        }
    }
}