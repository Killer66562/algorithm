class Buzzer {
    private:
        unsigned int pin;
    public:
        void tone();
        void notone();
        void beep(unsigned int freq, unsigned int times, unsigned int delay);
};