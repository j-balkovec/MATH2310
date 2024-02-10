#include <iostream>
#include <fstream>
#include <string>

// Abstract base class for loggers
class Logger {
public:
    virtual ~Logger() {}
    virtual void log(const std::string& message) = 0;
};

// Console logger
class ConsoleLogger : public Logger {
public:
    void log(const std::string& message) override {
        std::cout << "[ConsoleLogger] " << message << std::endl;
    }
};

// File logger
class FileLogger : public Logger {
private:
    std::ofstream file;

public:
    FileLogger(const std::string& filename) {
        file.open(filename, std::ofstream::out | std::ofstream::app);
    }

    ~FileLogger() {
        if (file.is_open())
            file.close();
    }

    void log(const std::string& message) override {
        if (file.is_open()) {
            file << "[FileLogger] " << message << std::endl;
            file.flush();
        }
    }
};

// Abstract base class for formatters
class Formatter {
public:
    virtual ~Formatter() {}
    virtual std::string format(const std::string& message) = 0;
};

// Default formatter
class DefaultFormatter : public Formatter {
public:
    std::string format(const std::string& message) override {
        return message;
    }
};

// Threaded logger decorator
class ThreadedLogger : public Logger {
private:
    Logger& logger;

public:
    ThreadedLogger(Logger& logger) : logger(logger) {}

    void log(const std::string& message) override {
        // Add threading logic here
        logger.log(message);
    }
};

int main() {
    // Create loggers and formatters
    ConsoleLogger consoleLogger;
    FileLogger fileLogger("log.txt");
    DefaultFormatter formatter;

    // Use loggers
    consoleLogger.log(formatter.format("Hello, console logger!"));
    fileLogger.log(formatter.format("Hello, file logger!"));

    // Use threaded logger
    ThreadedLogger threadedLogger(consoleLogger);
    threadedLogger.log(formatter.format("Hello, threaded console logger!"));

    return 0;
}
