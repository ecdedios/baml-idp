// Defining a data model.
class Appointment {
  day_of_week string
  month string
  date int
  year int
  hour int
  minute int
  ampm string
}

// Create a function to extract the resume from a string.
function ExtractAppointmentFromImage(appointment_card: image) -> Appointment {
  // Specify a client as provider/model-name
  // you can use custom LLM params with a custom client name from clients.baml like "client CustomHaiku"
  client "openai/gpt-4oMini" // Set OPENAI_API_KEY to use this client.
  prompt #"
    Extract details from this image of an appointment card reminder:
    {{ appointment_card }}

    {{ ctx.output_format }}
  "#
}

// TESTS
test Test_APPOINTMENT {
functions [ExtractAppointmentFromImage]
  args {
    img {
      url "#"
    }
  }
}
