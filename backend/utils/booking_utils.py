from backend.exceptions.booking_exception import BookingException


class BookingUtils:
    @staticmethod
    def is_booking_date_free(reserved_apartments, check_in, check_out):
        for reserved_apartment in reserved_apartments:
            if reserved_apartment:
                start = reserved_apartment.booking_start
                end = reserved_apartment.booking_end

                print(start)
                print(end)
                print(check_in)
                print(check_out)
                if start < check_in < end:
                    raise BookingException
                if start < check_out < end:
                    raise BookingException
                if check_in < start < check_out:
                    raise BookingException
                if check_in < start < check_out:
                    raise BookingException
